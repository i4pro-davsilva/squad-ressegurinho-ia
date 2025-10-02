import type { Config } from 'tailwindcss'
import tailwindcssAnimate from 'tailwindcss-animate'

export default {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#FAFAFA',
        primaryAccent: '#18181B',
        brand: '#f26423',
        i4pro: {
          orange: '#f26423',
          turquoise: '#28bebe',
          darkBlue: '#1E3A4C',
          gray: '#4d4d4d'
        },
        background: {
          DEFAULT: '#111113',
          secondary: '#27272A'
        },
        secondary: '#f5f5f5',
        border: 'rgba(var(--color-border-default))',
        accent: '#27272A',
        muted: '#A1A1AA',
        destructive: '#E53935',
        positive: '#22C55E',
        purple: {
          500: '#8B5CF6',
          600: '#7C3AED'
        },
        pink: {
          500: '#EC4899',
          600: '#DB2777'
        }
      },
      fontFamily: {
        geist: 'var(--font-geist-sans)',
        dmmono: 'var(--font-dm-mono)'
      },
      borderRadius: {
        xl: '12px',
        '2xl': '16px'
      },
      boxShadow: {
        'glow': '0 0 15px rgba(139, 92, 246, 0.3)',
        'glow-lg': '0 0 30px rgba(139, 92, 246, 0.4)',
        'glow-i4pro': '0 0 20px rgba(242, 100, 35, 0.3)',
        'glow-i4pro-lg': '0 0 30px rgba(242, 100, 35, 0.4)'
      }
    }
  },
  plugins: [tailwindcssAnimate]
} satisfies Config
