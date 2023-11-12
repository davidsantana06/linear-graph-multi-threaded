
let data;

window.addEventListener('load', () => {
  fetch("../output/graph.json")
    .then(response => {
      if (!response.ok) {
          throw new Error('Erro ao carregar o arquivo JSON');
      }
      return response.json();
  })
  .then(responseJSON => {
      data = responseJSON;
      generate()
  })
  .catch(error => {
      console.error('Erro:', error);
  });
})

function generate() {
  const graph = data.paths;

  const content = document.getElementById("content");
  for (let i = 0; i < graph.length; i++) {
    const path = graph[i];
    
    const nodeWrapper = document.createElement("div");
    nodeWrapper.classList.add("path-wrapper");

    const title = document.createElement("h1");
    title.innerHTML = `Caminho ${i + 1}`;

    const nodes = document.createElement("div");
    nodes.classList.add("nodes");

    for (let i = 0; i < 3; i++) {
      const node = document.createElement("div");
      node.classList.add("node");
      node.innerText = i + 1;
      nodes.appendChild(node);
    }

    const node = document.createElement("div");
    node.classList.add("node");
    node.innerText = path.length;
    nodes.appendChild(node);

    const total = document.createElement("span");
    total.innerText = `+ ${path.length - 3}`;
    nodes.appendChild(total);

    const edge = document.createElement("div");
    edge.classList.add("edge");
    nodes.appendChild(edge)

    nodeWrapper.appendChild(title)
    nodeWrapper.appendChild(nodes)

    content.appendChild(nodeWrapper);

  }

}