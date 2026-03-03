// Vietnamese math formula types for "Khao sat ham so" (Toan 12 THPT)

function fmt(n, v, plus) {
    if (n === 0) return ""
    const sign = n > 0 ? (plus ? " + " : "") : " - "
    const abs = Math.abs(n)
    const c = abs === 1 && v ? "" : String(abs)
    return `${sign}${c}${v}`
}

export const FORMULA_CONFIGS = {
    bac3: {
        type: "bac3",
        label: "Ham bac 3",
        description: "y = ax\u00B3 + bx\u00B2 + cx + d",
        coefficients: [
            { name: "a", label: "a", min: -5, max: 5, step: 0.1 },
            { name: "b", label: "b", min: -10, max: 10, step: 0.1 },
            { name: "c", label: "c", min: -10, max: 10, step: 0.1 },
            { name: "d", label: "d", min: -10, max: 10, step: 0.1 },
        ],
        evaluate: (x, [a, b, c, d]) => a * x ** 3 + b * x ** 2 + c * x + d,
        evaluateDerivative: (x, [a, b, c]) => 3 * a * x ** 2 + 2 * b * x + c,
        formatFormula: ([a, b, c, d]) => {
            const parts = []
            if (a !== 0) parts.push(fmt(a, "x\u00B3", false))
            if (b !== 0) parts.push(fmt(b, "x\u00B2", parts.length > 0))
            if (c !== 0) parts.push(fmt(c, "x", parts.length > 0))
            if (d !== 0) parts.push(fmt(d, "", parts.length > 0))
            return "y = " + (parts.join("").trim() || "0")
        },
        defaultCoeffs: [1, -3, 0, 2],
        xRange: [-5, 5],
    },
    bac2: {
        type: "bac2",
        label: "Ham bac 2",
        description: "y = ax\u00B2 + bx + c",
        coefficients: [
            { name: "a", label: "a", min: -5, max: 5, step: 0.1 },
            { name: "b", label: "b", min: -10, max: 10, step: 0.1 },
            { name: "c", label: "c", min: -10, max: 10, step: 0.1 },
        ],
        evaluate: (x, [a, b, c]) => a * x ** 2 + b * x + c,
        evaluateDerivative: (x, [a, b]) => 2 * a * x + b,
        formatFormula: ([a, b, c]) => {
            const parts = []
            if (a !== 0) parts.push(fmt(a, "x\u00B2", false))
            if (b !== 0) parts.push(fmt(b, "x", parts.length > 0))
            if (c !== 0) parts.push(fmt(c, "", parts.length > 0))
            return "y = " + (parts.join("").trim() || "0")
        },
        defaultCoeffs: [1, 0, -4],
        xRange: [-6, 6],
    },
    bac4tp: {
        type: "bac4tp",
        label: "Trung phuong",
        description: "y = ax\u2074 + bx\u00B2 + c",
        coefficients: [
            { name: "a", label: "a", min: -3, max: 3, step: 0.1 },
            { name: "b", label: "b", min: -10, max: 10, step: 0.1 },
            { name: "c", label: "c", min: -10, max: 10, step: 0.1 },
        ],
        evaluate: (x, [a, b, c]) => a * x ** 4 + b * x ** 2 + c,
        evaluateDerivative: (x, [a, b]) => 4 * a * x ** 3 + 2 * b * x,
        formatFormula: ([a, b, c]) => {
            const parts = []
            if (a !== 0) parts.push(fmt(a, "x\u2074", false))
            if (b !== 0) parts.push(fmt(b, "x\u00B2", parts.length > 0))
            if (c !== 0) parts.push(fmt(c, "", parts.length > 0))
            return "y = " + (parts.join("").trim() || "0")
        },
        defaultCoeffs: [1, -4, 3],
        xRange: [-4, 4],
    },
    phanthuoc: {
        type: "phanthuoc",
        label: "Phan thuc",
        description: "y = (ax + b) / (cx + d)",
        coefficients: [
            { name: "a", label: "a", min: -10, max: 10, step: 0.1 },
            { name: "b", label: "b", min: -10, max: 10, step: 0.1 },
            { name: "c", label: "c", min: -10, max: 10, step: 0.1 },
            { name: "d", label: "d", min: -10, max: 10, step: 0.1 },
        ],
        evaluate: (x, [a, b, c, d]) => {
            const den = c * x + d
            if (Math.abs(den) < 0.001) return null
            return (a * x + b) / den
        },
        evaluateDerivative: (x, [a, b, c, d]) => {
            const den = c * x + d
            if (Math.abs(den) < 0.001) return null
            return (a * d - b * c) / (den * den)
        },
        formatFormula: ([a, b, c, d]) => {
            const fmtLinear = (p, q) => {
                let s = ""
                if (p !== 0) s += p === 1 ? "x" : p === -1 ? "-x" : `${p}x`
                if (q > 0) s += s ? ` + ${q}` : `${q}`
                else if (q < 0) s += s ? ` - ${Math.abs(q)}` : `${q}`
                return s || "0"
            }
            return `y = (${fmtLinear(a, b)}) / (${fmtLinear(c, d)})`
        },
        defaultCoeffs: [2, 1, 1, -1],
        xRange: [-8, 8],
    },
}

export function analyzeFormula(type, coeffs) {
    const config = FORMULA_CONFIGS[type]
    const lines = []
    lines.push(config.formatFormula(coeffs))

    if (type === "bac3") {
        const [a, b, c] = coeffs
        lines.push("TXD: D = R")
        const delta = 4 * b * b - 12 * a * c
        if (a !== 0) {
            if (delta > 0) {
                const x1 = (-2 * b + Math.sqrt(delta)) / (6 * a)
                const x2 = (-2 * b - Math.sqrt(delta)) / (6 * a)
                const y1 = config.evaluate(x1, coeffs)
                const y2 = config.evaluate(x2, coeffs)
                lines.push(`y'=0: x = ${x1.toFixed(2)}, x = ${x2.toFixed(2)}`)
                if (y1 !== null && y2 !== null) {
                    if (a > 0) {
                        lines.push(`Cuc dai: (${x2.toFixed(2)}, ${y2.toFixed(2)})`)
                        lines.push(`Cuc tieu: (${x1.toFixed(2)}, ${y1.toFixed(2)})`)
                    } else {
                        lines.push(`Cuc dai: (${x1.toFixed(2)}, ${y1.toFixed(2)})`)
                        lines.push(`Cuc tieu: (${x2.toFixed(2)}, ${y2.toFixed(2)})`)
                    }
                }
            } else if (delta === 0) {
                lines.push("y'=0 co nghiem kep -> Khong co cuc tri")
            } else {
                lines.push("y'>0 hoac y'<0 -> Ham don dieu")
            }
        }
    }

    if (type === "bac2") {
        const [a, b, c] = coeffs
        lines.push("TXD: D = R")
        if (a !== 0) {
            const xv = -b / (2 * a)
            const yv = config.evaluate(xv, coeffs)
            lines.push(`Dinh: (${xv.toFixed(2)}, ${yv?.toFixed(2)})`)
            lines.push(a > 0 ? "Bề lom: Mo len" : "Bề lom: Mo xuong")
            const disc = b * b - 4 * a * c
            if (disc > 0) lines.push("Cat Ox tai 2 diem")
            else if (disc === 0) lines.push("Tiep xuc Ox")
            else lines.push("Khong cat Ox")
        }
    }

    if (type === "bac4tp") {
        const [a, b] = coeffs
        lines.push("TXD: D = R")
        lines.push("Ham chan: f(-x) = f(x)")
        if (a !== 0) {
            if (a > 0 && b < 0) lines.push("Co 2 cuc tieu va 1 cuc dai")
            else if (a > 0 && b >= 0) lines.push("Co 1 cuc tieu tai x = 0")
            else if (a < 0 && b > 0) lines.push("Co 2 cuc dai va 1 cuc tieu")
            else lines.push("Co 1 cuc dai tai x = 0")
        }
    }

    if (type === "phanthuoc") {
        const [a, b, c, d] = coeffs
        if (c !== 0) {
            const ax = -d / c
            const ay = a / c
            lines.push(`TXD: R \\ {${ax.toFixed(2)}}`)
            lines.push(`Tiem can dung: x = ${ax.toFixed(2)}`)
            lines.push(`Tiem can ngang: y = ${ay.toFixed(2)}`)
            const det = a * d - b * c
            lines.push(det > 0 ? "Dong bien tren tung khoang" : "Nghich bien tren tung khoang")
        }
    }

    return lines
}
