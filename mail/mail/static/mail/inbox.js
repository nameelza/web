document.addEventListener("DOMContentLoaded", function () {

    // Use buttons to toggle between views
    document.querySelector("#inbox").addEventListener("click", () => load_mailbox("inbox"));
    document.querySelector("#sent").addEventListener("click", () => load_mailbox("sent"));
    document.querySelector("#archived").addEventListener("click", () => load_mailbox("archive"));
    document.querySelector("#compose").addEventListener("click",() => compose_email({}));

    // By default, load the inbox
    load_mailbox("inbox");

});

function compose_email({body, sender, timestamp, subject}) {
  // Show compose view and hide other views
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "block";
  document.querySelector("#singleEmail-view").style.display = "none";

  // Clear out composition fields
  document.querySelector("#compose-recipients").value = sender || "";

  // Recipient disabled if replying to email
  if (sender) {
    document.querySelector("#compose-recipients").disabled = true;
  } else {
    document.querySelector("#compose-recipients").disabled = false;
  }

  if (subject && subject.startsWith("Re:")) {
      document.querySelector("#compose-subject").value = subject || "";
  } else {
      document.querySelector("#compose-subject").value = subject ? `Re: ${subject}` : "";
  }

  document.querySelector("#compose-body").value = body ? `On ${timestamp} ${sender} wrote: ${body} \n` : "";

  // Autofocus on body when replying to email
  if (body) {
    document.querySelector("#compose-body").focus();
  } 

  // Compose button sends the email
  document.querySelector("#compose-form").onsubmit = () => {
    const recipients = document.querySelector("#compose-recipients");
    const subject = document.querySelector("#compose-subject");
    const body = document.querySelector("#compose-body");
    fetch("/emails", {
      method: "POST",
      body: JSON.stringify({
        recipients: recipients.value,
        subject: subject.value,
        body: body.value,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.error) {
          let divAlert = document.createElement("div");
          divAlert.innerHTML = result.error;
          divAlert.className = "alert alert-danger";
          document.querySelector("#emails-view").appendChild(divAlert);
        } else if (result.message) {
          let divAlert = document.createElement("div");
          divAlert.innerHTML = result.message;
          divAlert.className = "alert alert-success";
          document.querySelector("#emails-view").appendChild(divAlert);
        }
      });
      // update and load the sent box after sending
      load_mailbox("sent");
      load_mailbox("sent");
      return false;
  };
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector("#emails-view").style.display = "block";
  document.querySelector("#compose-view").style.display = "none";
  document.querySelector("#singleEmail-view").style.display = "none";
  // Show the mailbox name
  document.querySelector("#emails-view").innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch the emails
  fetch(`/emails/${mailbox}`)
    .then((response) => response.json())
    .then((emails) => {
      // For each email, add an element to the DOM
      emails.forEach((email) => {
        let div = document.createElement("div");
        div.className = "email";

        if (email.read === false) {
          div.id = "notReadEmail";
        } else {
          div.id = "readEmail";
        }

        div.dataset.id = `${email.id}`;

        let divSender = document.createElement("div");
        divSender.className = "sender";
        let sender = document.createTextNode(`${email.sender}`);
        divSender.appendChild(sender);

        let divSubject = document.createElement("div");
        divSubject.className = "subject";
        let subject = document.createTextNode(`${email.subject}`);
        divSubject.appendChild(subject);

        let divTime = document.createElement("div");
        divTime.className = "timestamp";
        let time = document.createTextNode(`${email.timestamp}`);
        divTime.appendChild(time);

        div.appendChild(divSender);
        div.appendChild(divSubject);
        div.appendChild(divTime);
        document.querySelector("#emails-view").appendChild(div);
      });

      // Add event listeners to each email
      document.querySelectorAll(".email").forEach((email) => {
        email.onclick = () => {
          fetch(`/emails/${email.dataset.id}`)
            .then((response) => response.json())
            .then((email) => {

              // Email is now read
              fetch(`/emails/${email.id}`, {
                method: "PUT",
                body: JSON.stringify({
                  read: true
                })
              });

              // Show the email view and hide other views
              document.querySelector("#emails-view").style.display = "none";
              document.querySelector("#compose-view").style.display = "none";
              document.querySelector("#singleEmail-view").style.display = "block";

              // Show the email
              document.querySelector("#from").innerHTML = email.sender;
              document.querySelector("#to").innerHTML = email.recipients;
              document.querySelector("#subject").innerHTML = email.subject;
              document.querySelector("#body").innerHTML = email.body;
              document.querySelector("#timestamp").innerHTML = email.timestamp;

              // Hide reply button if mailbox is sent
              if (mailbox === "sent") {
                document.querySelector("#buttons").style.display = "none";
              } else {
                document.querySelector("#buttons").style.display = "block";
              }

              // Show archive or unarchive button, depending on whether the email is archived
              if (email.archived === true) {
                document.querySelector("#archive").innerHTML = "Unarchive";
              } else {
                document.querySelector("#archive").innerHTML = "Archive";
              }

              // Archive or unarchive the email
              document.querySelector('#archive').onclick = () => {
                if (email.archived === false) {
                  fetch(`/emails/${email.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                      archived: true
                    })
                  });
                  location.reload();
                } else {
                  fetch(`/emails/${email.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                      archived: false
                    })
                  });
                  location.reload();
                }
              };

              // Reply to the email
              document.querySelector("#reply").onclick = () => {
                  compose_email(email);
              }
            });
        };
      });
    });
}
