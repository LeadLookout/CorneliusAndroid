const { parentPort, workerData } = require('worker_threads');

// Perform heavy computation
function heavyComputation(data) {
  // ...perform heavy computation...
  return result;
}

const result = heavyComputation(workerData);
parentPort.postMessage(result);
