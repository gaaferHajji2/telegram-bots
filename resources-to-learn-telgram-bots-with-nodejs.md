Here are some of the best free resources for learning how to build **Telegram bots with Node.js**. Most tutorials focus on two popular libraries:

- **node-telegram-bot-api** (simpler for beginners, polling-based)
- **Telegraf** (more modern, middleware-friendly, great for complex bots and TypeScript)

Start with the official **Telegram Bot API** docs for core concepts (creating a bot via @BotFather, tokens, methods like sendMessage, handling updates via polling or webhooks):  
https://core.telegram.org/bots/api

### Free Tutorials and Guides
- **GitHub Tutorial for node-telegram-bot-api** (beginner-friendly step-by-step):  
  https://github.com/hosein2398/node-telegram-bot-api-tutorial  
  Covers BotFather setup, basic commands, and examples.

- **GeeksforGeeks: How to create a Telegram Chatbot with Node.js** (uses node-telegram-bot-api, includes echo bot example):  
  https://www.geeksforgeeks.org/node-js/how-to-create-telegram-chatbot-with-node-js/

- **Medium: Build a Telegram Bot with Node.js in 30 Minutes** (quick start with node-telegram-bot-api):  
  https://medium.com/@mike7830705/how-to-build-a-telegram-bot-with-node-js-in-30-minutes-56cb0f78d375

- **Telegraf Series on DEV Community** (TypeScript + Telegraf + Fastify for scalable bots, multi-part):  
  https://dev.to/6akcuk/your-own-telegram-bot-on-nodejs-with-typescript-telegraf-and-fastify-part-1-4f3l (and follow-up parts).

- **Hashnode: Telegram bot with Node.js and Telegraf** (practical example with responses and formatting):  
  https://vedanshmehra.hashnode.dev/telegram-bot-with-nodejs-and-telegraf

- **Official Telegraf Documentation** (highly recommended once you pick the library):  
  https://telegraf.js.org/ (includes examples and full API support).

- **node-telegram-bot-api GitHub Docs** (usage, examples, tutorials section):  
  https://github.com/yagop/node-telegram-bot-api

Other solid written guides include Sanity.io's meme bot tutorial and various Medium/HackerNoon articles for specific features like webhooks, databases, or AI integration.

### Free YouTube Tutorials and Playlists
- **"Master Telegram Bot Development using Node JS"** by Lets build together (comprehensive step-by-step):  
  https://www.youtube.com/watch?v=CALd9wiJCmI

- **"Creating a telegram bot using Node JS"** by Lets build together (covers setup, ngrok for local testing):  
  https://www.youtube.com/watch?v=COLDiMlmcoI

- **Telegram Bot Development Using Node.js and Telegraf API** (full playlist covering basics to deployment):  
  https://www.youtube.com/playlist?list=PLH7dcNRdf-1CLfP4KXqeVSww_76cAs1tY

- **"Learn Telegram bot development using Nodejs telegraf library"** (playlist with intro to BotFather and Telegraf):  
  https://www.youtube.com/playlist?list=PLjEYzWkdEvxvJ8lZacERw_NiUKbB7l_dx

- **"Building a Telegram Bot with Node.js"** by Mikhail Mikhaylov (talk-style overview):  
  https://www.youtube.com/watch?v=pxhXZFRixuY

Search YouTube for "Telegram bot Node.js Telegraf" or "Telegram bot Node.js node-telegram-bot-api" for many more short tutorials (10-30 minutes each).

### Free Courses
- **Udemy (free version available via Class Central)**: "Create Telegram bot with NodeJS and Firebase Cloud Functions" (uses Telegraf + deployment):  
  Check https://www.classcentral.com/course/udemy-telegram-firebase-bot-150372 for access.

- **Learncafe free course**: "Learn Telegram Bot Development Using Node.js Telegraf Library" (covers JS basics to Bot API integration).

### Libraries to Choose From
- **Telegraf** (recommended for most users): `npm install telegraf` — modern, extensible. GitHub: https://github.com/telegraf/telegraf
- **node-telegram-bot-api**: `npm install node-telegram-bot-api` — straightforward for simple bots. GitHub: https://github.com/yagop/node-telegram-bot-api

### Tips to Get Started
1. Create your bot with **@BotFather** in Telegram to get a token.
2. Use polling for quick local testing (or ngrok/webhooks for production).
3. Add features like commands (`bot.command()` in Telegraf), keyboards, or inline queries.
4. For deployment: Free options include Heroku (older), Render, Railway, or serverless like Firebase/ Vercel/Netlify (with webhooks).

These resources should take you from zero to a functional bot quickly. Start with a basic echo bot, then add commands, databases (e.g., Prisma), or external APIs. If you want advanced topics (scalability, TypeScript, AI integration), many of the linked articles cover them. Happy bot-building!