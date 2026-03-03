import { RotateCcw } from "lucide-react"
import { FORMULA_CONFIGS } from "../lib/formula.js"

const TYPES = [
    { value: "bac3", label: "Bac 3" },
    { value: "bac2", label: "Bac 2" },
    { value: "bac4tp", label: "Trung phuong" },
    { value: "phanthuoc", label: "Phan thuc" },
]

export function CoefficientPanel({
    formulaType,
    coefficients,
    showDerivative,
    onFormulaTypeChange,
    onCoefficientChange,
    onShowDerivativeChange,
    onReset,
}) {
    const config = FORMULA_CONFIGS[formulaType]

    return (
        <div className="flex flex-col gap-4 border-t border-border bg-background px-5 py-4">
            {/* Row 1: Formula type tabs + formula display + controls */}
            <div className="flex items-center justify-between gap-4">
                {/* Type selector as minimal tabs */}
                <div className="flex items-center gap-1">
                    {TYPES.map((t) => (
                        <button
                            key={t.value}
                            onClick={() => onFormulaTypeChange(t.value)}
                            className={`rounded-md px-2.5 py-1 text-[11px] font-medium transition-colors ${formulaType === t.value
                                    ? "bg-[#22d3ee]/10 text-[#22d3ee]"
                                    : "text-muted-foreground/60 hover:text-muted-foreground"
                                }`}
                        >
                            {t.label}
                        </button>
                    ))}
                </div>

                {/* Active formula */}
                <span className="font-mono text-xs text-foreground/70">
                    {config.formatFormula(coefficients)}
                </span>

                {/* Derivative toggle + reset */}
                <div className="flex items-center gap-2">
                    <button
                        onClick={() => onShowDerivativeChange(!showDerivative)}
                        className={`rounded-md px-2 py-1 text-[11px] font-medium transition-colors ${showDerivative
                                ? "bg-muted text-foreground/80"
                                : "text-muted-foreground/40 hover:text-muted-foreground/70"
                            }`}
                    >
                        {"y\u2019"}
                    </button>
                    <button
                        onClick={onReset}
                        className="flex items-center gap-1 text-muted-foreground/40 transition-colors hover:text-muted-foreground"
                        aria-label="Reset"
                    >
                        <RotateCcw className="size-3" />
                    </button>
                </div>
            </div>

            {/* Row 2: Coefficient sliders — using native range inputs */}
            <div className="flex items-start gap-5">
                {config.coefficients.map((coeff, i) => (
                    <div key={coeff.name} className="flex flex-1 flex-col gap-1.5">
                        <div className="flex items-center justify-between">
                            <span className="font-mono text-[11px] font-semibold text-[#22d3ee]/70">
                                {coeff.label}
                            </span>
                            <span className="font-mono text-[11px] tabular-nums text-foreground/60">
                                {coefficients[i]?.toFixed(1)}
                            </span>
                        </div>
                        <input
                            type="range"
                            value={coefficients[i] ?? 0}
                            min={coeff.min}
                            max={coeff.max}
                            step={coeff.step}
                            onChange={(e) => onCoefficientChange(i, parseFloat(e.target.value))}
                            className="w-full accent-[#22d3ee]"
                        />
                        <div className="flex justify-between">
                            <span className="text-[9px] text-muted-foreground/30">{coeff.min}</span>
                            <span className="text-[9px] text-muted-foreground/30">{coeff.max}</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
