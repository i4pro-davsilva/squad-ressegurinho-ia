'use client'

import type React from 'react'

import { motion, AnimatePresence } from 'framer-motion'
import { useStickToBottomContext } from 'use-stick-to-bottom'

import { Button } from '@/components/ui/button'
import Icon from '@/components/ui/icon'

const ScrollToBottom: React.FC = () => {
  const { isAtBottom, scrollToBottom } = useStickToBottomContext()

  return (
    <AnimatePresence>
      {!isAtBottom && (
        <motion.div
          initial={{ opacity: 0, y: 20, scale: 0.8 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          exit={{ opacity: 0, y: 20, scale: 0.8 }}
          transition={{ duration: 0.3, ease: [0.4, 0, 0.2, 1] }}
          className="absolute bottom-6 left-1/2 -translate-x-1/2"
        >
          <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}>
            <Button
              onClick={() => scrollToBottom()}
              type="button"
              size="icon"
              variant="secondary"
              className="glass-effect h-12 w-12 rounded-full border-0 bg-accent/80 text-primary shadow-xl ring-1 ring-white/20 transition-all duration-300 hover:bg-accent hover:shadow-2xl hover:shadow-purple-500/20"
            >
              <Icon type="arrow-down" size="xs" />
            </Button>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}

export default ScrollToBottom
