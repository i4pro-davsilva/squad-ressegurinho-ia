'use client'

import Link from 'next/link'
import { motion, Variants } from 'framer-motion'
import Icon from '@/components/ui/icon'
import { IconType } from '@/components/ui/icon/types'
import React, { useState } from 'react'

const EXTERNAL_LINKS = {
  documentation: 'https://www.i4pro.com.br/pt',
  website: 'https://www.i4pro.com.br/pt/erp',
  contact: 'https://www.i4pro.com.br/pt/contato'
}

const TECH_ICONS = [
  {
    type: 'python' as IconType,
    position: 'left-0',
    link: 'https://www.python.org',
    name: 'Python',
    zIndex: 10
  },
  {
    type: 'database' as IconType,
    position: 'left-[25px]',
    link: '#',
    name: 'SQL Database',
    zIndex: 20
  },
  {
    type: 'globe' as IconType,
    position: 'left-[55px]',
    link: '#',
    name: 'REST API',
    zIndex: 30
  }
]

interface ActionButtonProps {
  href: string
  variant?: 'primary'
  text: string
}

const ActionButton = ({ href, variant, text }: ActionButtonProps) => {
  const baseStyles =
    'px-6 py-3 text-sm font-semibold transition-all duration-300 font-dmmono tracking-wide uppercase'
  const variantStyles = {
    primary: 'glass-effect bg-gradient-to-r from-i4pro-orange to-i4pro-turquoise text-white shadow-lg shadow-i4pro-orange/30 hover:shadow-xl hover:shadow-i4pro-orange/40 hover:scale-105 rounded-xl ring-1 ring-i4pro-orange/50'
  }

  return (
    <Link
      href={href}
      target="_blank"
      className={`${baseStyles} ${variant ? variantStyles[variant] : 'glass-effect bg-accent/50 ring-1 ring-white/10 hover:bg-accent/70 hover:ring-white/20 hover:scale-105 rounded-xl'}`}
    >
      {text}
    </Link>
  )
}

const ChatBlankState = () => {
  const [hoveredIcon, setHoveredIcon] = useState<string | null>(null)

  // Animation variants for the icon
  const iconVariants: Variants = {
    initial: { y: 0 },
    hover: {
      y: -8,
      transition: {
        type: 'spring',
        stiffness: 150,
        damping: 10,
        mass: 0.5
      }
    },
    exit: {
      y: 0,
      transition: {
        type: 'spring',
        stiffness: 200,
        damping: 15,
        mass: 0.6
      }
    }
  }

  // Animation variants for the tooltip
  const tooltipVariants: Variants = {
    hidden: {
      opacity: 0,
      transition: {
        duration: 0.15,
        ease: 'easeInOut'
      }
    },
    visible: {
      opacity: 1,
      transition: {
        duration: 0.15,
        ease: 'easeInOut'
      }
    }
  }

  return (
    <section
      className="flex flex-col items-center text-center font-geist"
      aria-label="Welcome message"
    >
      <div className="flex max-w-4xl flex-col gap-y-10">
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-4xl font-[600] tracking-tight leading-relaxed"
        >
          <div className="flex items-center justify-center gap-x-2 whitespace-nowrap font-medium">
            <span className="flex items-center font-[600] bg-gradient-to-r from-i4pro-turquoise to-i4pro-orange bg-clip-text text-transparent">
              Agente de IA
            </span>
            <span className="inline-flex translate-y-[10px] scale-125 items-center transition-transform duration-200 hover:rotate-6 hover:scale-150">
              <Link
                href={EXTERNAL_LINKS.website}
                target="_blank"
                rel="noopener"
                className="cursor-pointer mx-8"
              >
                <img src="/assets/i4pro-logo.svg" alt="i4pro" className="h-24 w-auto" />
              </Link>
            </span>
            <span className="flex items-center font-[600] bg-gradient-to-r from-i4pro-orange to-i4pro-turquoise bg-clip-text text-transparent">
              by Resseguro Team
            </span>
            <span className="inline-flex translate-y-[5px] scale-125 items-center">
              <div className="relative ml-2 h-[40px] w-[90px]">
                {TECH_ICONS.map((icon) => (
                  <motion.div
                    key={icon.type}
                    className={`absolute ${icon.position} top-0`}
                    style={{ zIndex: icon.zIndex }}
                    variants={iconVariants}
                    initial="initial"
                    whileHover="hover"
                    animate={hoveredIcon === icon.type ? 'hover' : 'exit'}
                    onHoverStart={() => setHoveredIcon(icon.type)}
                    onHoverEnd={() => setHoveredIcon(null)}
                  >
                    <Link
                      href={icon.link}
                      target="_blank"
                      rel="noopener"
                      className="relative block cursor-pointer"
                    >
                      <div className="transition-all duration-300 hover:drop-shadow-[0_0_8px_rgba(242,100,35,0.5)]">
                        <Icon type={icon.type} size="default" />
                      </div>
                      <motion.div
                        className="pointer-events-none absolute bottom-full left-1/2 mb-2 -translate-x-1/2 transform whitespace-nowrap rounded-lg glass-effect bg-accent/90 px-3 py-1.5 text-xs font-medium text-primary ring-1 ring-white/20 shadow-lg"
                        variants={tooltipVariants}
                        initial="hidden"
                        animate={
                          hoveredIcon === icon.type ? 'visible' : 'hidden'
                        }
                      >
                        {icon.name}
                      </motion.div>
                    </Link>
                  </motion.div>
                ))}
              </div>
            </span>
          </div>
          <p className="mt-4 text-2xl text-secondary/90">Soluções inteligentes para o mercado de seguros</p>
        </motion.h1>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="flex justify-center gap-5"
        >
          <ActionButton
            href={EXTERNAL_LINKS.website}
            variant="primary"
            text="NOSSOS PRODUTOS"
          />
          <ActionButton href={EXTERNAL_LINKS.contact} text="Entre em contato" />
        </motion.div>
      </div>
    </section>
  )
}

export default ChatBlankState
