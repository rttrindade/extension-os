chrome.runtime.onInstalled.addListener(function(){
    chrome.contextMenus.create({
        id:"gerarOs",
        title: "Gerar Os",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener(function(info, tab){
    if(info.menuItemId === "gerarOs") {
        console.log("Texto Selecionado:", info.selectionText);
        document.getElementById("textoColado").innerHTML = info.selectionText;
        chrome.sidePanel.open({ windowId: tab.windowId});
        
    }
});