const mainDiv = document.querySelector('.main');
const ENDPOINT = 'http://127.0.0.1:8000';

const getData = async(route) => {
    const data = await fetch(`${ENDPOINT}/${route}`);
    return await data.json();
};

const createElement = (tag, className, text, innerHTML) => {
    const element = document.createElement(tag);
    if(className) element.className = className;
    if(text) element.textContent = text;
    if(innerHTML) element.innerHTML += innerHTML;
    return element;
};

const renderItems = (items) => {
    mainDiv.innerHTML = '';
    
    items.forEach(element => {
        user = element.tasks
        const userName = createElement('h3', 'userName', `${element.username}`)
        mainDiv.append(userName)
        for (let i of user){
            const deadL = i.dead_line.slice(0, 10);
            const startD = i.start_date.slice(0, 10);
            const task = createElement('div', 'task');
            const title = createElement('h1', 'title', `${i.title}`);
            const description = createElement('p', 'description', `${i.description}`);
            const deadLine = createElement('p', 'deadLine', `${deadL}`);
            const status = createElement('p', 'status', `${i.status}`);
            const startDate = createElement('p', 'startDate', `${startD}`);
            task.append(title, description, startDate, deadLine, status);
            mainDiv.append(task);
        };
        
    });
};


getData('task-list/').then(renderItems);