const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  host: 'smtp.meta.ua',
  port: 465,
  secure: true,
  auth: {
    user: 'rakushka324@meta.ua',
    pass: 'Macksim14@',
  },
});

async function sendEmail({ userName, userEmail, userText }) {
  const emailContant = ` 
  <h2 style="color: green;">Ви отримали листа від ${userName}</h2
  <p>email для контактів ${userEmail}</p>
  <p>Текст повідомлення: ${userText}</p>
  <p style="color: blue;">Дякуємо. Гарного дня.</p>
  `;
  const info = await transporter.sendMail({
    from: 'rakushka324@meta.ua', // sender address
    to: 'kardmitriy@gmail.com', // list of receivers
    subject: 'Звернення від користувача до директора', // Subject line
    text: userText, // plain text body
    html: emailContant, // html body
  });

  console.log('Message sent: %s', info.messageId);
}

module.exports = sendEmail;
