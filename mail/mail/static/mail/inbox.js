document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Compose button sends the email
  document.querySelector('#compose-form').onsubmit = function () {
    const recipients = document.querySelector('#compose-recipients');
    const subject = document.querySelector('#compose-subject');
    const body = document.querySelector('#compose-body');
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipients.value,
          subject: subject.value,
          body: body.value
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
        console.log(result.message);
        // Redirect to sent view
        load_mailbox('sent');
    });
  }

}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch the emails
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // Add each email to the DOM
      emails.forEach(email => {
        if (email.read === false) {
          document.querySelector('#emails-view').innerHTML +=
          `<div class="email" id="notReadEmail">
            <div class="sender">${email.sender}</div>
            <div class="subject">${email.subject}</div>
            <div class="timestamp">${email.timestamp}</div>
          </div>`;
        } else {
          document.querySelector('#emails-view').innerHTML +=
          `<div class="email" id="readEmail">
            <div class="sender">${email.sender}</div>
            <div class="subject">${email.subject}</div>
            <div class="timestamp">${email.timestamp}</div>
          </div>`;
        }
      });
  });
}