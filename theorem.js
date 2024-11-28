// Theorem 1
function maxProbability1(p, k) {
    return (2 + 2 * Math.sqrt(p / (1 - p))) * Math.pow(4 * p * (1 - p), k);
}

function minProbability1(p, k) {
    return Math.pow(4 * p * (1 - p), k) / Math.sqrt(k);
}

function p1(i, p) {
    return Math.pow((1 - p) / p, i - 1) * (1 - (1 - p) / p);
}

function p2(j, n, q) {
    return math.comb(n, j) * Math.pow(q, j) * Math.pow((1 - q), (n - j));
}

function f1(i, p) {
    return Math.pow((1 - p) / p, i);
}

function f2(j, n, q) {
    let sum = 0;
    for (let l = j + 1; l <= n; l++) {
        sum += p2(l, n, q);
    }
    return sum;
}

// Theorem 2
function maxProbability2(k, p) {
    let total = f1(k, p);
    for (let i = 1; i <= k; i++) {
        let inner = 0;
        for (let j = 0; j <= k - i; j++) {
            inner += p2(j, 2 * k + 1 - i, 1 - p) * f1(2 * k + 1 - 2 * i - 2 * j, p);
        }
        total += p1(i, p) * (f2(k - i, 2 * k + 1 - i, 1 - p) + inner);
    }

    return total;
}

function minProbability2(k, p) {
    let total = f1(k, p);
    for (let i = 1; i <= k; i++) {
        let inner = 0;
        for (let j = 0; j <= k - i; j++) {
            inner += p2(j, 2 * k + 1 - i, 1 - p) * f1(2 * k + 2 - 2 * i - 2 * j, p);
        }
        total += p1(i, p) * (f2(k - i, 2 * k + 1 - i, 1 - p) + inner);
    }

    return total;
}

// Test cases
// console.log(maxProbability1(0.75, 11));
// console.log(minProbability1(0.75, 11));
console.log(maxProbability2(0, 0.6));
console.log(minProbability2(0, 0.6));
// console.log(maxProbability2(40, 0.75));
// console.log(minProbability2(40, 0.75));
// console.log(maxProbability2(60, 0.75));
// console.log(minProbability2(60, 0.75));
