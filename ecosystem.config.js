module.exports = {
  apps: [
    {
      name: 'Face Image Spoof Detection API',
      script: 'python',
      args: 'run_api.py',
      exec_mode: 'fork',
      autorestart: true,
      watch: false,
      env: {
        NODE_ENV: 'production',
      }
    }
  ]
};



