
window.addEventListener('DOMContentLoaded', () => {
    

    let todos = JSON.parse(localStorage.getItem('todos_cad')) || [
        {
            nome: "Entregar Laudo PCD",
            desc: "Laudo médico para comprovação",
            area: "Médica",
            prog: 50,
            etapas: [
                { nome: "Consulta marcada com especialista.", prog: 100 },
                { nome: "Realizar exames solicitados.", prog: 50 },
                { nome: "Aguardando resultado dos exames.", prog: 0 }
            ]
        },
        {
            nome: "Diploma de Graduação",
            desc: "Entregar cópia autenticada",
            area: "Documentação",
            prog: 100,
            etapas: []
        }
    ];

    const todoListContainer = document.getElementById('todo-list');

    function renderTodos() {
        todoListContainer.innerHTML = '';
        todos.forEach((todo, idx) => {
            const todoRow = document.createElement('div');
            todoRow.className = 'todo-row row gy-2 gx-2 align-items-center';
            todoRow.dataset.id = idx;

            // Gera o HTML para uma única tarefa
            todoRow.innerHTML = `
                <div class="col-auto"><span class="handle"><i class="bi bi-list"></i></span></div>
                <div class="col-md-2"><b>${todo.nome}</b></div>
                <div class="col-md-3">${todo.desc || ''}</div>
                <div class="col-md-1"><span class="badge bg-secondary">${todo.area || ''}</span></div>
                <div class="col-md-3">
                    <div class="progress" role="progressbar" aria-valuenow="${todo.prog}" aria-valuemin="0" aria-valuemax="100" style="height: 20px;">
                        <div class="progress-bar ${getBarClass(todo.prog)}" style="width: ${todo.prog}%">${todo.prog}%</div>
                    </div>
                </div>
                <div class="col-md-2 todo-actions text-end">
                    <button class="btn btn-primary btn-sm todo-ctrl" type="button" title="Editar Tarefa" onclick="loadToEdit(${idx})"><i class="bi bi-pencil"></i></button>
                    <button class="btn btn-danger btn-sm todo-ctrl" type="button" title="Excluir Tarefa" onclick="removerTodo(${idx})"><i class="bi bi-trash"></i></button>
                    <button class="btn btn-secondary btn-sm todo-ctrl" type="button" title="Ver/Adicionar Etapas" onclick="toggleEtapas(${idx})"><i class="bi bi-list-check"></i></button>
                </div>
                <div class="col-12 etapas-area" id="etapas-${idx}" style="display: none;">
                    <h6><i class="bi bi-diagram-3"></i> Etapas</h6>
                    <div id="etapa-list-${idx}">
                        ${(todo.etapas || []).map((e, ei) => etapaHtml(idx, ei, e)).join('')}
                    </div>
                    <div class="row mt-2 g-2 align-items-end">
                        <div class="col"><input type="text" class="form-control form-control-sm" id="etapa-nome-${idx}" placeholder="Nome da nova etapa"></div>
                        <div class="col-3 col-md-2"><input type="number" min="0" max="100" id="etapa-prog-${idx}" class="form-control form-control-sm" placeholder="%"></div>
                        <div class="col-auto">
                            <button type="button" class="btn btn-success btn-sm" onclick="addEtapa(${idx})"><i class="bi bi-plus"></i> Adicionar Etapa</button>
                        </div>
                    </div>
                </div>
            `;
            todoListContainer.appendChild(todoRow);
        });
        saveAndRerender();
    }
    
    // Função que gera o HTML para uma etapa (sub-tarefa)
    function etapaHtml(todoIndex, etapaIndex, etapa) {
        return `
        <div class="etapa-row row align-items-center gx-2">
            <div class="col">${etapa.nome}</div>
            <div class="col-4 col-md-3">
                <div class="progress" style="height: 1rem;">
                    <div class="progress-bar ${getBarClass(etapa.prog)}" style="width: ${etapa.prog}%">${etapa.prog}%</div>
                </div>
            </div>
            <div class="col-auto">
                <button class="btn btn-warning btn-sm etapa-ctrl" onclick="editEtapa(${todoIndex}, ${etapaIndex})"><i class="bi bi-pencil"></i></button>
                <button class="btn btn-danger btn-sm etapa-ctrl" onclick="removerEtapa(${todoIndex}, ${etapaIndex})"><i class="bi bi-trash"></i></button>
            </div>
        </div>`;
    }

    // Adiciona uma nova tarefa principal
    window.addToDo = function() {
        const form = document.getElementById('todo-form');
        const nome = document.getElementById('todo-nome').value.trim();
        if (!nome) return;

        todos.push({
            nome: nome,
            desc: document.getElementById('todo-desc').value.trim(),
            area: document.getElementById('todo-area').value,
            prog: parseInt(document.getElementById('todo-prog').value) || 0,
            etapas: []
        });
        form.reset();
        document.getElementById('todo-prog').value = '0';
        saveAndRerender();
    }

    // Carrega os dados de uma tarefa no formulário para edição
    window.loadToEdit = function(idx) {
        const item = todos[idx];
        document.getElementById('todo-nome').value = item.nome;
        document.getElementById('todo-desc').value = item.desc;
        document.getElementById('todo-area').value = item.area;
        document.getElementById('todo-prog').value = item.prog;
        removerTodo(idx, false);
    }

    // Remove uma tarefa principal
    window.removerTodo = function(idx, rerender = true) {
        todos.splice(idx, 1);
        if(rerender) saveAndRerender();
    }
    
    // Altera o progresso de uma tarefa no formulário principal
    window.alterInputProg = function(delta) {
        const inp = document.getElementById('todo-prog');
        let valor = parseInt(inp.value) || 0;
        inp.value = Math.max(0, Math.min(100, valor + delta));
    }

    // Mostra ou esconde a área de etapas
    window.toggleEtapas = function(idx) {
        const d = document.getElementById(`etapas-${idx}`);
        d.style.display = (d.style.display === "none" ? "block" : "none");
    }

    // Adiciona uma nova etapa a uma tarefa
    window.addEtapa = function(idx) {
        const nomeInput = document.getElementById(`etapa-nome-${idx}`);
        const progInput = document.getElementById(`etapa-prog-${idx}`);
        const nome = nomeInput.value.trim();
        if (!nome) return;

        todos[idx].etapas = todos[idx].etapas || [];
        todos[idx].etapas.push({
            nome: nome,
            prog: parseInt(progInput.value) || 0
        });
        
        nomeInput.value = '';
        progInput.value = '';
        saveAndRerender();
        document.getElementById(`etapas-${idx}`).style.display = 'block';
    }
    
    // Remove uma etapa
    window.removerEtapa = function(idx, etapaIdx) {
        todos[idx].etapas.splice(etapaIdx, 1);
        saveAndRerender();
        document.getElementById(`etapas-${idx}`).style.display = 'block';
    }

    // Carrega os dados de uma etapa para edição
    window.editEtapa = function(idx, etapaIdx) {
        const etapa = todos[idx].etapas[etapaIdx];
        document.getElementById(`etapa-nome-${idx}`).value = etapa.nome;
        document.getElementById(`etapa-prog-${idx}`).value = etapa.prog;
        removerEtapa(idx, etapaIdx);
    }

    // Retorna a classe CSS da barra de progresso com base no valor
    function getBarClass(prog) {
        if (prog >= 80) return "bg-success";
        if (prog >= 40) return "bg-warning";
        return "bg-danger";
    }

    // Salva no localStorage
    function saveAndRerender() {
        localStorage.setItem('todos_cad', JSON.stringify(todos));
        renderTodos();
    }

    // Função "arrastar e soltar"
    new Sortable(todoListContainer, {
        handle: '.handle',
        animation: 150,
        onEnd: function (evt) {
            
            const [movedItem] = todos.splice(evt.oldIndex, 1);
            todos.splice(evt.newIndex, 0, movedItem);
            
            // Salva a nova ordem e re-renderiza para atualizar os índices
            saveAndRerender();
        },
    });

    renderTodos();

});
