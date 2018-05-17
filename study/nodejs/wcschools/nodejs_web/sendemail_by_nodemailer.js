var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'uvmaker@gmail.com',
    pass: 'tlove759***'
  }
});

var mailOptions = {
  from: 'uvmaker@gmail.com',
  to: 'uvmaker@naver.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
