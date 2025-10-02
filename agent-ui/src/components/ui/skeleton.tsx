import { cn } from '@/lib/utils'

const Skeleton = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => {
  return (
    <div
      className={cn('shimmer animate-pulse rounded-xl glass-effect bg-accent/30 ring-1 ring-white/5', className)}
      {...props}
    />
  )
}

export { Skeleton }
