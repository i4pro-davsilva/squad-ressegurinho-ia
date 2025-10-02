'use client'

import ChatInput from './ChatInput'
import MessageArea from './MessageArea'
const ChatArea = () => {
  return (
    <main className="relative m-2 flex flex-grow flex-col rounded-2xl glass-effect shadow-xl overflow-hidden">
      <MessageArea />
      <div className="sticky bottom-0 ml-9 px-6 pb-6 pt-4 bg-gradient-to-t from-background/95 via-background/80 to-transparent">
        <ChatInput />
      </div>
    </main>
  )
}

export default ChatArea
