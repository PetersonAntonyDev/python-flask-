class Tasks {
    constructor() {
        this.id = 1;
    }

    adicionar() {
        let task = this.lerDados;
    }

    lerDados() {
        let task = {}

        task.id = this.id;
        task.taksname = document.getElementById("task").value;

        return task
    }
}