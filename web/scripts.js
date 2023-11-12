const generate = async () => {
  const graph = await getPaths();

  const content = document.getElementById("content");
  content.innerHTML = "";
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
    nodes.appendChild(edge);

    nodeWrapper.appendChild(title);
    nodeWrapper.appendChild(nodes);

    content.appendChild(nodeWrapper);
  }
}

const solve = async () => {
  await generate();
  const solution = await getSolution();
  setNodeClass(solution.best.id - 1, "best")
  setNodeClass(solution.worst.id - 1, "worst")
}

const setNodeClass = (id, classe) => {
  const content = document.getElementById("content");
  const path = content.getElementsByClassName('path-wrapper')[id];
  const nodes = path.querySelector(".nodes");
  nodes.classList.add(classe)
}

const getSolution = async () => {
  return await fetch("../output/solution.json")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Erro ao carregar o arquivo JSON");
    }
    return response.json();
  })
  .then((response) => {
    return response;
  })
  .catch((error) => {
    console.error("Erro:", error);
  });
}

const getPaths = async () => {
  return await fetch("../output/graph.json")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Erro ao carregar o arquivo JSON");
    }
    return response.json();
  })
  .then((response) => {
    return response.paths;
  })
  .catch((error) => {
    console.error("Erro:", error);
  });
}