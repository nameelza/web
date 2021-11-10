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
  document.querySelector('#singleEmail-view').style.display = 'none';

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
    document.querySelector('#singleEmail-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // Fetch the emails
    fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails);

        // For each email, add an element to the DOM
        emails.forEach(email => {
            let div = document.createElement('div');
            div.className = "email";

            if (email.read === false) {
              div.id = "notReadEmail";
            } else {
              div.id = "readEmail";
            }

            div.dataset.id = `${email.id}`

            let divSender = document.createElement('div')
            divSender.className = "sender";
            let sender = document.createTextNode(`${email.sender}`);
            divSender.appendChild(sender);

            let divSubject = document.createElement('div')
            divSubject.className = "subject";
            let subject = document.createTextNode(`${email.subject}`);
            divSubject.appendChild(subject);

            let divTime = document.createElement('div')
            divTime.className = "timestamp";
            let time = document.createTextNode(`${email.timestamp}`);
            divTime.appendChild(time);

            div.appendChild(divSender);
            div.appendChild(divSubject);
            div.appendChild(divTime);
            console.log(div);
            document.querySelector('#emails-view').appendChild(div);

        });

        // Add event listeners to each email
        document.querySelectorAll('.email').forEach(email => {
            email.onclick = () => {
                fetch(`/emails/${email.dataset.id}`)
                .then(response => response.json())
                .then(email => {
                    // Print email
                    console.log(email);
                    document.querySelector('#emails-view').style.display = 'none';
                    document.querySelector('#singleEmail-view').style.display = 'block';

                    let spanFrom = document.createElement('span');
                    let from = document.createTextNode(`${email.sender}`);
                    spanFrom.appendChild(from);
                    document.querySelector('#from').appendChild(spanFrom);

                    let spanTo = document.createElement('span');
                    let to = document.createTextNode(`${email.recipients}`);
                    spanTo.appendChild(to);
                    document.querySelector('#to').appendChild(spanTo);

                    let spanSubject = document.createElement('span');
                    let subject = document.createTextNode(`${email.subject}`);
                    spanSubject.appendChild(subject);
                    document.querySelector('#subject').appendChild(spanSubject);

                    let spanTimestamp = document.createElement('span');
                    let timestamp = document.createTextNode(`${email.timestamp}`);
                    spanTimestamp.appendChild(timestamp);
                    document.querySelector('#timestamp').appendChild(spanTimestamp);

                    let spanBody = document.createElement('span');
                    let body = document.createTextNode(`${email.body}`);
                    spanBody.appendChild(body);
                    document.querySelector('#body').appendChild(spanBody);

                });
            }
        });
    });
}
