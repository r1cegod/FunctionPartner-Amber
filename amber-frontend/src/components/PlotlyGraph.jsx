import { useMemo } from "react"
import Plot from "react-plotly.js"
import { FORMULA_CONFIGS } from "../lib/formula.js"

export function PlotlyGraph({ formulaType, coefficients, showDerivative }) {
    const { data, layout } = useMemo(() => {
        const config = FORMULA_CONFIGS[formulaType]
        const [xMin, xMax] = config.xRange
        const numPoints = 800
        const step = (xMax - xMin) / numPoints

        const xVals = []
        const yVals = []
        const dyVals = []

        for (let i = 0; i <= numPoints; i++) {
            const x = xMin + i * step
            xVals.push(x)
            const y = config.evaluate(x, coefficients)
            if (y === null || Math.abs(y) > 80) {
                yVals.push(null)
            } else {
                yVals.push(y)
            }

            if (showDerivative) {
                const dy = config.evaluateDerivative(x, coefficients)
                if (dy === null || Math.abs(dy) > 80) {
                    dyVals.push(null)
                } else {
                    dyVals.push(dy)
                }
            }
        }

        const traces = [
            {
                x: xVals,
                y: yVals,
                type: "scatter",
                mode: "lines",
                name: config.formatFormula(coefficients),
                line: { color: "#22d3ee", width: 2.5, shape: "spline" },
                connectgaps: false,
                hovertemplate: "x = %{x:.2f}<br>y = %{y:.3f}<extra></extra>",
            },
        ]

        if (showDerivative && dyVals.length > 0) {
            traces.push({
                x: xVals,
                y: dyVals,
                type: "scatter",
                mode: "lines",
                name: "y\u2019",
                line: { color: "#737373", width: 1.5, dash: "dot", shape: "spline" },
                connectgaps: false,
                opacity: 0.6,
                hovertemplate: "x = %{x:.2f}<br>y' = %{y:.3f}<extra></extra>",
            })
        }

        // Special points: extrema (cuc tri)
        const spX = []
        const spY = []
        const spL = []

        if (formulaType === "bac3") {
            const [a, b, c] = coefficients
            const delta = 4 * b * b - 12 * a * c
            if (delta > 0 && a !== 0) {
                const x1 = (-2 * b + Math.sqrt(delta)) / (6 * a)
                const x2 = (-2 * b - Math.sqrt(delta)) / (6 * a)
                const y1 = config.evaluate(x1, coefficients)
                const y2 = config.evaluate(x2, coefficients)
                if (y1 !== null && Math.abs(y1) < 80) { spX.push(x1); spY.push(y1); spL.push("Cuc tri") }
                if (y2 !== null && Math.abs(y2) < 80) { spX.push(x2); spY.push(y2); spL.push("Cuc tri") }
            }
        }

        if (formulaType === "bac2" && coefficients[0] !== 0) {
            const xv = -coefficients[1] / (2 * coefficients[0])
            const yv = config.evaluate(xv, coefficients)
            if (yv !== null) { spX.push(xv); spY.push(yv); spL.push("Dinh") }
        }

        if (formulaType === "bac4tp") {
            const [a, b] = coefficients
            if (a !== 0) {
                const y0 = config.evaluate(0, coefficients)
                if (y0 !== null) { spX.push(0); spY.push(y0); spL.push("Cuc tri") }
                const ratio = -b / (2 * a)
                if (ratio > 0) {
                    const xc = Math.sqrt(ratio)
                    const yc1 = config.evaluate(xc, coefficients)
                    const yc2 = config.evaluate(-xc, coefficients)
                    if (yc1 !== null) { spX.push(xc); spY.push(yc1); spL.push("Cuc tri") }
                    if (yc2 !== null) { spX.push(-xc); spY.push(yc2); spL.push("Cuc tri") }
                }
            }
        }

        if (spX.length > 0) {
            traces.push({
                x: spX,
                y: spY,
                type: "scatter",
                mode: "markers+text",
                name: "Diem dac biet",
                marker: { color: "#22d3ee", size: 7, symbol: "circle", line: { color: "#0a0a0a", width: 2 } },
                text: spL,
                textposition: "top center",
                textfont: { size: 10, color: "#67e8f9" },
                hovertemplate: "%{text}<br>(%{x:.2f}, %{y:.3f})<extra></extra>",
            })
        }

        // Asymptotes for phanthuoc
        if (formulaType === "phanthuoc") {
            const [a, , c, d] = coefficients
            if (c !== 0) {
                const ax = -d / c
                const ay = a / c
                traces.push({
                    x: [ax, ax], y: [-80, 80],
                    type: "scatter", mode: "lines",
                    name: `TC\u0110: x=${ax.toFixed(1)}`,
                    line: { color: "#404040", width: 1, dash: "dash" },
                    hoverinfo: "skip",
                })
                traces.push({
                    x: [xMin, xMax], y: [ay, ay],
                    type: "scatter", mode: "lines",
                    name: `TCN: y=${ay.toFixed(1)}`,
                    line: { color: "#404040", width: 1, dash: "dash" },
                    hoverinfo: "skip",
                })
            }
        }

        return {
            data: traces,
            layout: {
                paper_bgcolor: "transparent",
                plot_bgcolor: "transparent",
                font: { color: "#737373", family: "monospace", size: 11 },
                margin: { l: 48, r: 16, t: 16, b: 40 },
                xaxis: {
                    gridcolor: "rgba(255,255,255,0.04)",
                    zerolinecolor: "rgba(34,211,238,0.2)",
                    zerolinewidth: 1,
                    tickfont: { size: 10 },
                    dtick: 1,
                    range: [xMin, xMax],
                },
                yaxis: {
                    gridcolor: "rgba(255,255,255,0.04)",
                    zerolinecolor: "rgba(34,211,238,0.2)",
                    zerolinewidth: 1,
                    tickfont: { size: 10 },
                },
                legend: {
                    x: 0.01, y: 0.99,
                    bgcolor: "rgba(10,10,10,0.9)",
                    bordercolor: "rgba(255,255,255,0.06)",
                    borderwidth: 1,
                    font: { size: 10, color: "#999" },
                },
                hovermode: "closest",
                hoverlabel: {
                    bgcolor: "#1a1a1a",
                    bordercolor: "#22d3ee",
                    font: { color: "#e5e5e5", family: "monospace", size: 12 },
                },
                autosize: true,
                showlegend: false,
            },
        }
    }, [formulaType, coefficients, showDerivative])

    return (
        <Plot
            data={data}
            layout={layout}
            useResizeHandler
            config={{
                displayModeBar: true,
                modeBarButtonsToRemove: ["lasso2d", "select2d"],
                displaylogo: false,
                responsive: true,
            }}
            style={{ width: "100%", height: "100%" }}
        />
    )
}
