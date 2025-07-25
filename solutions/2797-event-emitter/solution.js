class EventEmitter {
    constructor(){
        this.map = {};
        this.key = 0
    }
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
       if(this.map[eventName] === undefined){
        this.map[eventName] = new Set()
       }

       this.map[eventName].add(callback);

        return {
            unsubscribe: () => {
                this.map[eventName].delete(callback);
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const out = []
        const fns = this.map[eventName]

        if(fns){
            for(const fn of fns){
                out.push(fn(...args));
            }
        }

        return out;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
