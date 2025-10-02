'use client'
import { useState } from 'react'
import { toast } from 'sonner'
import { TextArea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'
import { useStore } from '@/store'
import useAIChatStreamHandler from '@/hooks/useAIStreamHandler'
import { useQueryState } from 'nuqs'
import Icon from '@/components/ui/icon'
import { motion } from 'framer-motion'

const ChatInput = () => {
  const { chatInputRef } = useStore()

  const { handleStreamResponse } = useAIChatStreamHandler()
  const [selectedAgent] = useQueryState('agent')
  const [teamId] = useQueryState('team')
  const [inputMessage, setInputMessage] = useState('')
  const [isFocused, setIsFocused] = useState(false)
  const isStreaming = useStore((state) => state.isStreaming)
  const handleSubmit = async () => {
    if (!inputMessage.trim()) return

    const currentMessage = inputMessage
    setInputMessage('')

    try {
      await handleStreamResponse(currentMessage)
    } catch (error) {
      toast.error(
        `Error in handleSubmit: ${
          error instanceof Error ? error.message : String(error)
        }`
      )
    }
  }

  return (
    <motion.div
      className="relative mx-auto flex w-full max-w-3xl items-end justify-center gap-x-3 font-geist"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <div className="relative flex-1">
        <motion.div
          className="absolute -inset-[1px] rounded-2xl bg-gradient-to-r from-i4pro-orange/50 via-i4pro-turquoise/50 to-i4pro-orange/50 opacity-0 blur-sm transition-opacity duration-300"
          animate={{ opacity: isFocused ? 1 : 0 }}
        />
        <TextArea
          placeholder="Ask anything..."
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onFocus={() => setIsFocused(true)}
          onBlur={() => setIsFocused(false)}
          onKeyDown={(e) => {
            if (
              e.key === 'Enter' &&
              !e.nativeEvent.isComposing &&
              !e.shiftKey &&
              !isStreaming
            ) {
              e.preventDefault()
              handleSubmit()
            }
          }}
          className="relative w-full border-0 glass-effect bg-accent/80 px-5 py-3.5 text-sm text-primary placeholder:text-muted/60 shadow-lg transition-all duration-300 hover:bg-accent/90 focus:bg-accent/95 focus:shadow-xl"
          disabled={!(selectedAgent || teamId)}
          ref={chatInputRef}
        />
      </div>
      <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
        <Button
          onClick={handleSubmit}
          disabled={
            !(selectedAgent || teamId) || !inputMessage.trim() || isStreaming
          }
          size="icon"
          className="h-12 w-12 rounded-2xl bg-gradient-to-br from-i4pro-orange to-i4pro-turquoise text-white shadow-lg shadow-i4pro-orange/30 transition-all duration-300 hover:shadow-xl hover:shadow-i4pro-orange/40 disabled:from-accent disabled:to-accent disabled:shadow-none"
        >
          <Icon type="send" color="primary" />
        </Button>
      </motion.div>
    </motion.div>
  )
}

export default ChatInput
