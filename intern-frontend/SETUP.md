# Setup Instructions for Candidates

Welcome to the Frontend Intern Challenge! Follow these steps to get started.

## Prerequisites

Make sure you have installed:

- Node.js (version 18 or higher)
- npm (comes with Node.js)

Check your versions:

```bash
node --version
npm --version
```

## Setup Steps

1. **Navigate to the challenge folder**

   ```bash
   cd intern-frontend
   ```

2. **Install dependencies** (this may take a few minutes)

   ```bash
   npm install
   ```

3. **Open TWO terminal windows/tabs**

4. **In Terminal 1: Start the Mock API Server**

   ```bash
   npm run api
   ```

   You should see:

   ```
   ✅ Mock API server running at http://localhost:3000
   📡 Weather endpoint: http://localhost:3000/weather
   ```

5. **In Terminal 2: Start the Angular Development Server**

   ```bash
   npm start
   ```

   Wait until you see:

   ```
   ** Angular Live Development Server is listening on localhost:4200 **
   ```

6. **Open your browser**

   Navigate to: http://localhost:4200

7. **You're ready!** 🎉

   You should see "Weather Dashboard" with a message to complete the template.

## Testing the API

You can test if the API is working by visiting:
http://localhost:3000/weather

You should see JSON data with weather information for 5 cities.

## Troubleshooting

**Port already in use?**

- Kill the process using port 4200 or 3000
- Or change the port in angular.json (for Angular) or api-server.js (for API)

**Module not found errors?**

- Run `npm install` again
- Delete `node_modules` folder and `package-lock.json`, then run `npm install`

**Still having issues?**

- Ask the interviewer for help!

## Tips

- Save your files frequently (Cmd+S / Ctrl+S)
- The browser will auto-reload when you save
- Check the browser console (F12) for errors
- Check the terminal for compilation errors

Good luck! 🚀
