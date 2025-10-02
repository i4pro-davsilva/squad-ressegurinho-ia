import Icon from '@/components/ui/icon'
import MarkdownRenderer from '@/components/ui/typography/MarkdownRenderer'
import { useStore } from '@/store'
import type { ChatMessage } from '@/types/os'
import Videos from './Multimedia/Videos'
import Images from './Multimedia/Images'
import Audios from './Multimedia/Audios'
import { memo } from 'react'
import AgentThinkingLoader from './AgentThinkingLoader'
import { motion } from 'framer-motion'

interface MessageProps {
  message: ChatMessage
}

const AgentMessage = ({ message }: MessageProps) => {
  const { streamingErrorMessage } = useStore()
  let messageContent
  if (message.streamingError) {
    messageContent = (
      <div className="rounded-2xl glass-effect border border-red-500/20 bg-red-500/5 px-5 py-4">
        <p className="text-sm text-red-400">
          Oops! Something went wrong while streaming.{' '}
          {streamingErrorMessage ? (
            <>{streamingErrorMessage}</>
          ) : (
            'Please try refreshing the page or try again later.'
          )}
        </p>
      </div>
    )
  } else if (message.content) {
    messageContent = (
      <div className="flex w-full flex-col gap-4">
        <MarkdownRenderer>{message.content}</MarkdownRenderer>
        {message.videos && message.videos.length > 0 && (
          <Videos videos={message.videos} />
        )}
        {message.images && message.images.length > 0 && (
          <Images images={message.images} />
        )}
        {message.audio && message.audio.length > 0 && (
          <Audios audio={message.audio} />
        )}
      </div>
    )
  } else if (message.response_audio) {
    if (!message.response_audio.transcript) {
      messageContent = (
        <div className="mt-2 flex items-start">
          <AgentThinkingLoader />
        </div>
      )
    } else {
      messageContent = (
        <div className="flex w-full flex-col gap-4">
          <MarkdownRenderer>
            {message.response_audio.transcript}
          </MarkdownRenderer>
          {message.response_audio.content && message.response_audio && (
            <Audios audio={[message.response_audio]} />
          )}
        </div>
      )
    }
  } else {
    messageContent = (
      <div className="mt-2">
        <AgentThinkingLoader />
      </div>
    )
  }

  return (
    <motion.div
      className="group flex flex-row items-start gap-4 font-geist"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <div className="flex-shrink-0 mt-1">
        <div className="rounded-xl bg-gradient-to-br from-purple-500/20 to-pink-600/20 p-2 ring-1 ring-purple-500/30 transition-all duration-300 group-hover:ring-purple-500/50 group-hover:shadow-lg group-hover:shadow-purple-500/20">
          <Icon type="agent" size="sm" />
        </div>
      </div>
      <div className="flex-1 min-w-0">{messageContent}</div>
    </motion.div>
  )
}

const UserMessage = memo(({ message }: MessageProps) => {
  return (
    <motion.div
      className="group flex items-start gap-4 pt-4 text-start max-md:break-words"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <div className="flex-shrink-0 mt-1">
        <div className="rounded-xl bg-accent/50 p-2 ring-1 ring-white/10 transition-all duration-300 group-hover:ring-white/20 group-hover:bg-accent/70">
          <Icon type="user" size="sm" />
        </div>
      </div>
      <div className="flex-1 min-w-0 rounded-2xl glass-effect bg-accent/30 px-5 py-4 text-base leading-relaxed text-secondary/95 shadow-md transition-all duration-300 group-hover:bg-accent/40 group-hover:shadow-lg">
        {message.content}
      </div>
    </motion.div>
  )
})

AgentMessage.displayName = 'AgentMessage'
UserMessage.displayName = 'UserMessage'
export { AgentMessage, UserMessage }
