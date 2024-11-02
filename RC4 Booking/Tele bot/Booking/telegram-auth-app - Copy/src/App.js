import React from 'react';
import TelegramLoginButton from 'react-telegram-login';

const handleTelegramResponse = response => {
  console.log("Telegram Response:", response);
  // Handle the response data as needed, such as sending it to your backend
};

function App() {
  return (
    <div className="App">
      <h1>Telegram Login</h1>
      <TelegramLoginButton
        dataOnauth={handleTelegramResponse}
        botName="rc4bookingbot"  // Replace with your bot's username
      />
    </div>
  );
}

export default App;
