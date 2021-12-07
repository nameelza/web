document.addEventListener("DOMContentLoaded", function () {
  const editButton = document.querySelectorAll(".edit");
  editButton.forEach((element) => {
    element.addEventListener("click", function () {
      const id = element.getAttribute("data-id");
      const content = document.querySelector(`#content-${id}`);

      // Create textarea
      const area = document.createElement("textarea");
      area.className = "form-control w-100";
      area.id = `content-${id}`;
      area.value = content.innerHTML;

      // Replace content with textarea
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
        saveButton.style.display = "none";
        element.style.display = "block";
        fetch("/edit", {
          method: "PUT",
          body: JSON.stringify({
            post_id: id,
            content: content.innerHTML,
          }),
        })
      });
    });
  });
});
