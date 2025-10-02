'use client'

import * as React from 'react'
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem
} from '@/components/ui/select'
import { useStore } from '@/store'
import { useQueryState } from 'nuqs'
import useChatActions from '@/hooks/useChatActions'

export function ModeSelector() {
  const { mode, setMode, setMessages, setSelectedModel } = useStore()
  const { clearChat } = useChatActions()
  const [, setAgentId] = useQueryState('agent')
  const [, setTeamId] = useQueryState('team')
  const [, setSessionId] = useQueryState('session')

  const handleModeChange = (newMode: 'agent' | 'team') => {
    if (newMode === mode) return

    setMode(newMode)

    setAgentId(null)
    setTeamId(null)
    setSelectedModel('')
    setMessages([])
    setSessionId(null)
    clearChat()
  }

  return (
    <>
      <Select
        defaultValue={mode}
        value={mode}
        onValueChange={(value) => handleModeChange(value as 'agent' | 'team')}
      >
        <SelectTrigger className="h-10 w-full rounded-xl glass-effect border-0 bg-accent/50 text-xs font-semibold uppercase tracking-wide ring-1 ring-white/10 transition-all duration-300 hover:bg-accent/70 hover:ring-white/20 focus:ring-2 focus:ring-purple-500/50">
          <SelectValue />
        </SelectTrigger>
        <SelectContent className="rounded-xl glass-effect border border-white/10 bg-accent/95 font-dmmono shadow-xl backdrop-blur-md">
          <SelectItem value="agent" className="cursor-pointer rounded-lg transition-colors duration-200 hover:bg-purple-500/20 focus:bg-purple-500/20">
            <div className="text-xs font-semibold uppercase tracking-wide">Agent</div>
          </SelectItem>

          <SelectItem value="team" className="cursor-pointer rounded-lg transition-colors duration-200 hover:bg-purple-500/20 focus:bg-purple-500/20">
            <div className="text-xs font-semibold uppercase tracking-wide">Team</div>
          </SelectItem>
        </SelectContent>
      </Select>
    </>
  )
}
