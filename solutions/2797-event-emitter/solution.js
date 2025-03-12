class EventEmitter {
    constructor(){
        this.events = new Map();
        this.key = 0
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        const prevEvents = this.events.get(eventName) ?? new Map()
        

        prevEvents.set(this.key, callback)
        this.events.set(eventName, prevEvents)
        let eventKey = this.key
        this.key += 1

        return {
            unsubscribe: () => {
                prevEvents.delete(eventKey)
                return undefined
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const output = []
        const events = this.events.get(eventName)?.values() ?? []
        console.log(events)

        for(const cb of events){
            output.push(cb(...args))
        }

        return output
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
