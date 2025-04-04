export class Logger {
    static log(message: string) {
        console.log(`[LOG] ${message}`);
    }

    static error(message: string) {
        console.error(`[ERROR] ${message}`);
    }

    static debug(message: string) {
        console.debug(`[DEBUG] ${message}`);
    }
}
