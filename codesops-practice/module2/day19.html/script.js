let cart = document.createElement("strong");
cart.textContent="cart"
let newdiv = document.createElement("div")
newdiv.appendChild(cart)
document.getElementById("nav-bar").appendChild(newdiv)
newdiv.classList.add("blue")
cart.addEventListener("click", () => {alert("cart was clicked")})

let form = document.getElementById("form")
form.addEventListener("submit" , function (event) {
    event.preventDefault();
    console.log("from submitted");
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    console.log("email:" ; email);
    console.log("password:"; password);
    

});



// TODO: Hold items in an array (this is your single source of truth)
let items = [];

// TODO: Select necessary DOM elements (form, input, list, count)
const form = document.querySelector('form');
const input = document.querySelector('input');
const list = document.querySelector('#list');
const count = document.querySelector('#count');

// TODO: Write a render() function to rebuild the list from the array
function render() {
  // 1. Clear the current list
  list.innerHTML = "";

  // 2. Loop through the items array
  items.forEach(item => {
    // 3. Create elements, use data-id on each row, and append to the list
    const li = document.createElement('li');
    li.setAttribute('data-id', item.id);
    if (item.done) {
      li.classList.add('done');
    }

    li.innerHTML = 
      <span class="todo-text">${item.text}</span>
      <button class="delete-btn">Remove</button>
    ;
    list.appendChild(li);
  });

  // 4. Update the live count paragraph
  const activeCount = items.filter(item => !item.done).length;
  count.textContent = ${activeCount} item${activeCount === 1 ? '' : 's'} left;
}

// TODO: Handle form submission
form.addEventListener('submit', (e) => {
  // 1. preventDefault to stop page reload
  e.preventDefault();

  // 2. Read and validate the input
  const text = input.value.trim();
  if (!text) return;

  // 3. Push a new object to the items array
  items.push({
    id: Date.now().toString(),
    text: text,
    done: false
  });

  // 4. Call render()
  render();
  input.value = '';
});

// TODO: Set up event delegation on the #list
list.addEventListener('click', (e) => {
  // 1. Listen for clicks on the parent <ul> & 2. Find clicked row
  const row = e.target.closest('[data-id]');
  if (!row) return;

  const id = row.getAttribute('data-id');

  // 3. Determine if the user is toggling ".done" or removing a row
  if (e.target.classList.contains('delete-btn')) {
    // 4. Update the items array (Remove)
    items = items.filter(item => item.id !== id);
  } else {
    // 4. Update the items array (Toggle Done)
    items = items.map(item => {
      if (item.id === id) {
        return { ...item, done: !item.done };
      }
      return item;
    });
  }

  // 5. Call render()
  render();
});