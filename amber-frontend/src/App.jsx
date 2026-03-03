import { useState, useCallback } from 'react'
import { FORMULA_CONFIGS } from './lib/formula.js'
import { ChatSidebar } from './components/ChatSidebar.jsx'
import { PlotlyGraph } from './components/PlotlyGraph.jsx'
import { CoefficientPanel } from './components/CoefficientPanel.jsx'

function App() {
  /*set states*/
  const [messages, setMessages] = useState([
    {
      id: "welcome",
      role: "assistant",
      content: "Nhap cong thuc de bat dau ve do thi.\nVi du: x^3 - 3x + 2",
    },
  ])
  const [input, setInput] = useState("")
  const [showDerivative, setShowDerivative] = useState(false)
  const [formulaType, setFormulaType] = useState("bac3")
  const [coefficients, setCoefficients] = useState(FORMULA_CONFIGS.bac3.defaultCoeffs)
  const [defaultType, setdefaultType] = useState("bac3")
  const [defaultcoefficients, setdefaultcoefficients] = useState(FORMULA_CONFIGS.bac3.defaultCoeffs)

  /*formula handler*/
  const handleFormulaTypeChange = useCallback((type) => {
    setFormulaType(type)
    setCoefficients([...FORMULA_CONFIGS[type].defaultCoeffs])
  }, [])
  const handleCoefficientChange = useCallback((index, value) => {
    setCoefficients((prev) => {
      const next = [...prev]
      next[index] = value
      return next
    })
  }, [])
  const handleReset = useCallback(() => {
    setFormulaType(defaultType)
    setCoefficients(defaultcoefficients)
    setShowDerivative(false)
  }, [defaultType, defaultcoefficients])

  /*messages handler*/
  const handleSend = useCallback(
    async (text) => {
      const msg = (text || input).trim()
      if (!msg) return

      const userMsg = { id: Date.now().toString(), role: "user", content: msg }
      const typingMsg = { id: "typing", role: "assistant", content: "", isTyping: true }

      setMessages((prev) => [...prev, userMsg, typingMsg])
      setInput("")
      const response = await
        fetch("http://localhost:8000/user_chat",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
          })
      const data = await response.json()
      if (data.graph) {
        setFormulaType(data.graph.type)
        setCoefficients(data.graph.coefficients)
        setdefaultType(data.graph.type)
        setdefaultcoefficients(data.graph.coefficients)
      }
      const reply = data.messages.at(-1).content
      setMessages((prev) => prev.filter((m) => m.id !== "typing").concat({
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: reply,
      })
      )
    },
    [input]
  )
  return (
    <div className="flex h-screen flex-col overflow-hidden bg-background">
      {/* header */}
      <header className="flex shrink-0 items-center border-b border-border px-6 py-3">
        <span className="text-sm font-semibold text-foreground">Amber</span>
        <span className="mx-2 text-xs text-muted-foreground/40">|</span>
        <span className="text-xs text-muted-foreground/60">function partner</span>
      </header>
      {/*just the chat, full width */}
      <div className="flex flex-1 overflow-hidden">
        <main className="flex flex-[4] flex-col overflow-hidden">
          {/*graph area*/}
          <div className="flex-1 overflow-hidden">
            <PlotlyGraph
              formulaType={formulaType}
              coefficients={coefficients}
              showDerivative={showDerivative}
            />
          </div>

          {/*coefficient panel beneath graph*/}
          <CoefficientPanel
            formulaType={formulaType}
            coefficients={coefficients}
            showDerivative={showDerivative}
            onFormulaTypeChange={handleFormulaTypeChange}
            onCoefficientChange={handleCoefficientChange}
            onShowDerivativeChange={setShowDerivative}
            onReset={handleReset}
          />
        </main>
        <aside className="flex w-[340px] shrink-0 flex-col overflow-hidden">
          <ChatSidebar
            messages={messages}
            onSend={handleSend}
            input={input}
            setInput={setInput}
          />
        </aside>
      </div>
    </div>
  )
}

export default App
