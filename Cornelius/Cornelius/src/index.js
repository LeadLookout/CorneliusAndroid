const config = require('../config/production.json');
const express = require('express');
const app = express();

// ...existing code...

// Use production configurations
app.set('trust proxy', 1); // Trust first proxy
app.use(require('helmet')()); // Secure app by setting various HTTP headers

// ...existing code...

// Optimize main thread by offloading heavy computations
const { Worker } = require('worker_threads');

function runHeavyComputation(data) {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./heavyComputation.js', { workerData: data });
    worker.on('message', resolve);
    worker.on('error', reject);
    worker.on('exit', (code) => {
      if (code !== 0) reject(new Error(`Worker stopped with exit code ${code}`));
    });
  });
}

// ...existing code...

app.listen(config.port, () => {
  console.log(`Server running in production mode on port ${config.port}`);
});
