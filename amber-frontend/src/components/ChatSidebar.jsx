import { useState, useRef, useEffect, useCallback } from "react"
import { Send } from "lucide-react"

function ChatMessage({ message, index }) {
    const isUser = message.role === "user"
    return (
        <div className="flex flex-col items-start" style={{
            animation: `floatIn 0.35s ease-out ${Math.min(index * 0.04, 0.3)}s both`,
        }}>
            {isUser ?
                (<div className="rounded-2xl rounded-bl-sm bg-[#1a1a1a] px-3.5 py-2 text-[13px] leading-relaxed text-foreground/90">
                    {message.content}
                </div>) :
                message.isTyping ? (
                    <div className="flex items-center gap-1 py-2">
                        <span className="size-1 rounded-full bg-muted-foreground/60" style={{ animation: "dotPulse 1.4s infinite", animationDelay: "0ms" }} />
                        <span className="size-1 rounded-full bg-muted-foreground/60" style={{ animation: "dotPulse 1.4s infinite", animationDelay: "200ms" }} />
                        <span className="size-1 rounded-full bg-muted-foreground/60" style={{ animation: "dotPulse 1.4s infinite", animationDelay: "400ms" }} />
                    </div>) :
                    (<div className="flex flex-col gap-1 py-0.5">
                        {message.content.split("\n").map((line, i) => {
                            if (!line.trim()) return <div key={i} className="h-1" />
                            const isFormula = line.startsWith("y = ") || line.startsWith("y=") || line.match(/^(TXD|Cuc|Dinh|Tiem|Dong|Nghich|Cat|Tiep|Khong|Ham|Co |Bề)/)
                            return (
                                <span
                                    key={i}
                                    className={
                                        isFormula
                                            ? "font-mono text-[12px] leading-relaxed text-[#22d3ee]/80"
                                            : "text-[13px] leading-relaxed text-muted-foreground"
                                    }>
                                    {line}
                                </span>
                            )
                        })}
                    </div>
                    )}
        </div>
    )
}

const QUICK_EXAMPLES = [
    { formula: "x^2", label: "x²" },
    { formula: "x^3 - 3x + 2", label: "x³−3x+2" },
    { formula: "sin(x)", label: "sin(x)" },
]

export function ChatSidebar({ messages, onSend, input, setInput }) {
    const scrollRef = useRef(null)
    const scrollToBottom = useCallback(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight
        }
    }, [])

    useEffect(() => {
        scrollToBottom()
    }, [messages, scrollToBottom])

    const handleSend = useCallback((text) => {
        const msg = (text || input).trim()
        if (!msg) return
        onSend(msg)
    }, [input, onSend])

    return (
        <div className="flex h-full flex-col border-l border-border bg-background">
            {/* Messages area */}
            <div ref={scrollRef} className="flex-1 overflow-y-auto px-4 py-4">
                <div className="flex flex-col gap-3">
                    {messages.map((msg, i) => (
                        <ChatMessage key={msg.id} message={msg} index={i} />
                    ))}

                    {/* Quick examples after welcome */}
                    {messages.length <= 2 && (
                        <div className="flex flex-col gap-2 pt-2">
                            <span className="text-[10px] uppercase tracking-widest text-muted-foreground/40">
                                Thu nhanh
                            </span>
                            <div className="flex flex-wrap gap-1.5">
                                {QUICK_EXAMPLES.map((ex) => (
                                    <button
                                        key={ex.formula}
                                        onClick={() => handleSend(ex.formula)}
                                        className="rounded-lg border border-border bg-secondary/40 px-2.5 py-1.5 font-mono text-[11px] text-muted-foreground transition-colors hover:border-[#22d3ee]/30 hover:text-[#22d3ee]"
                                    >
                                        {ex.label}
                                    </button>
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            </div>

            {/* Input bar */}
            <div className="border-t border-border p-3">
                <div className="flex items-center gap-2 rounded-lg border border-border bg-secondary/30 px-3 py-2 transition-colors focus-within:border-[#22d3ee]/40">
                    <input
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === "Enter" && !e.shiftKey) {
                                e.preventDefault()
                                handleSend()
                            }
                        }}
                        placeholder="Nhap cong thuc..."
                        className="flex-1 bg-transparent text-[13px] text-foreground outline-none placeholder:text-muted-foreground/30"
                    />
                    <button
                        onClick={() => handleSend()}
                        disabled={!input.trim()}
                        className="flex size-7 items-center justify-center rounded-md text-muted-foreground transition-colors hover:text-[#22d3ee] disabled:opacity-20"
                        aria-label="Gui"
                    >
                        <Send className="size-3.5" />
                    </button>
                </div>
            </div>
        </div>
    )
}
