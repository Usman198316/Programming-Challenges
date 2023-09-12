let draggableElements = document.querySelectorAll(".draggable");
let droppableElements = document.querySelectorAll(".droppable");

function updateElements() {
  draggableElements = document.querySelectorAll(".draggable");
  droppableElements = document.querySelectorAll(".droppable");

  draggableElements.forEach(elem => {
    elem.classList.remove("anticlockwise")
    elem.classList.remove("clockwise")
    elem.addEventListener("dragstart", dragStart)
    elem.addEventListener("dragend", dragEnd)
})
droppableElements.forEach(elem => {
    elem.classList.remove("anticlockwise")
    elem.classList.remove("clockwise")
    elem.addEventListener("dragenter", dragEnter); 
    elem.addEventListener("dragover", dragOver); 
    elem.addEventListener("dragleave", dragLeave); 
    elem.addEventListener("drop", drop); 
})

}

updateElements();

// drag and drop

function dragStart(event) {
    event.dataTransfer.setData("text", event.target.id)

    draggableElements.forEach(elem => {
        if(!elem.classList.contains("droppable")) {
            elem.classList.add("droppable")
        }
        if(elem.classList.contains("draggable")) {
            elem.classList.remove("draggable")
        }
    })
   updateElements(); 

   const sourceElement = document.getElementById(event.dataTransfer.getData("text"));
   sourceElement.classList.add("dragging")
   const boxes = sourceElement.parentNode;
   const boxesChildren = Array.from(boxes.children);
   boxesChildren.forEach(box => {
    if (boxesChildren.indexOf(box) < boxesChildren.indexOf(sourceElement)) {
        box.classList.add("anticlockwise")
    } else if (boxesChildren.indexOf(box) > boxesChildren.indexOf(sourceElement)) {
        box.classList.add("clockwise")
    } 

   })

}

function dragEnter(event) {
    event.target.classList.add("droppable-hover")
}

function dragLeave(event) {
    event.target.classList.remove("droppable-hover")
}

function dragOver(event) {
    event.preventDefault()
}

function dragEnd(event) {
    droppableElements.forEach(elem => {
        if(!elem.classList.contains("draggable")) {
            elem.classList.add("draggable")
        }
        if(elem.classList.contains("droppable")) {
            elem.classList.remove("droppable")
        }
    })
    updateElements();
    event.target.classList.remove("dragging")

}

function drop(event) {
    event.preventDefault();
    event.stopPropagation();
    event.target.classList.remove("droppable-hover")

    const targetElement = event.target;
    const sourceElement = document.getElementById(event.dataTransfer.getData("text"));

    const container = targetElement.parentNode;
    const containerChildren = Array.from(container.children);

    const targetIndex = containerChildren.indexOf(targetElement);
    const sourceIndex = containerChildren.indexOf(sourceElement);
    
    if (targetIndex == sourceIndex + 1) {
        container.insertBefore(sourceElement, containerChildren[targetIndex]);
        container.insertBefore(targetElement, containerChildren[sourceIndex]);
    } else {
        container.insertBefore(sourceElement, containerChildren[targetIndex]);
        container.insertBefore(targetElement, containerChildren[sourceIndex+1]);
    }

    droppableElements.forEach(elem => {
        if(!elem.classList.contains("draggable")) {
            elem.classList.add("draggable")
        }
        if(elem.classList.contains("droppable")) {
            elem.classList.remove("droppable")
        }
    })
    updateElements();

}
