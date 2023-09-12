const draggableElements = document.querySelectorAll(".draggable");
const droppableElements = document.querySelectorAll(".droppable")

draggableElements.forEach(elem => {
    elem.addEventListener("dragstart", dragStart);
    // elem.addEventListener("drag", drag);
    // elem.addEventListener("dragend", dragEnd);
});

droppableElements.forEach(elem => {
    elem.addEventListener("dragenter", dragEnter); // Fires when a dragged item enters a valid drop target
    elem.addEventListener("dragover", dragOver); // Fires when a dragged item is being dragged over a valid drop target, repeatedly while the draggable item is within the drop zone
    elem.addEventListener("dragleave", dragLeave); // Fires when a dragged item leaves a valid drop target
    elem.addEventListener("drop", drop); // Fires when an item is dropped on a valid drop target
  });

// drag and drop functions

function dragStart(event) {
    event.dataTransfer.setData("text", event.target.id)
}

function dragEnter(event) {
    if(!event.target.classList.contains("dropped")) {
        event.target.classList.add("droppable-hover");
    }
}

function dragLeave(event) {
    if(!event.target.classList.contains("dropped")) {
        event.target.classList.remove("droppable-hover");
    }
}

function dragOver(event) {
    if(!event.target.classList.contains("dropped")) {
        event.preventDefault();
    }
}

function drop(event){
    event.preventDefault();
    event.target.classList.remove("droppable-hover");
    const draggableElementData = event.dataTransfer.getData("text")
    const droppableElementData = event.target.getAttribute("data-draggable-id");
    if(draggableElementData === droppableElementData) {
        event.target.classList.add("dropped");
        const draggableElement = document.getElementById(draggableElementData)
        event.target.style.backgroundColor = draggableElement.style.color;
        draggableElement.classList.add("dragged");
        draggableElement.setAttribute("draggable", "false");
        event.target.insertAdjacentHTML("afterbegin", `<i class="fas fa-${draggableElementData}"></i>`);

    }
}
