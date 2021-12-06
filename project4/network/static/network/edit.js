document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM loaded");
  const editButton = document.querySelectorAll(".edit");
  editButton.forEach((element) => {
    element.addEventListener("click", function () {
      const id = element.getAttribute("data-id");
      const content = document.querySelector(`#content-${id}`);
      const temp = content.cloneNode(true);
      console.log("temp outside", temp);

      // Create textarea
      const area = document.createElement("textarea");
      area.className = "form-control w-100";
      area.id = `content-${id}`;
      area.value = content.innerHTML;
      console.log("Button clicked");
      console.log(id);

      // Replace content with textarea
      console.log("Run");
      console.log(content);
      content.replaceWith(area);

      // Add save button
      element.style.display = "none";
      const saveButton = document.createElement("div");
      saveButton.className = "save";
      saveButton.innerHTML = "Save";
      element.after(saveButton);

      saveButton.addEventListener("click", () => {
        content.innerHTML = area.value;
        area.replaceWith(content);
        console.log("save button clicked");
        saveButton.style.display = "none";
        element.style.display = "block";
      });

      console.log(content.innerHTML);
      console.log("temp first", temp);

      // console.log("temp second", temp);
      // console.log("area", area);
      // console.log(content.innerHTML);
      // temp.innerHTML = area.value;
      // area.replaceWith(temp);
      // // Change save button back to edit button
      // element.innerHTML = "Edit";
      // element.style.color = "black";
    });
  });
});
