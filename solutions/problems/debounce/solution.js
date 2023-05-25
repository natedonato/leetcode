var debounce = function(fn, t) {
    let int;
    return function(...args) {
        clearTimeout(int);
        int = setTimeout(() => fn(...args), t)
    }
};