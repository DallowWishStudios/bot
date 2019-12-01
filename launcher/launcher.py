import webbrowser
import time
import pyperclip
import tkinter
import pyautogui
import subprocess
from tkinter import messagebox
from pynput.keyboard import Key, Controller

botCode = 'bot&&bot.stop();{const t=(t,e=null,i=null)=>{e&&(t.id=controllerId),i&&t.classList.add(...i)},e=(t,e)=>{const i=t.classList.contains(\"btn-on\");return t.classList.toggle(\"btn-on\"),bot.text[e](i),i},i=(t,e,i)=>{var n=new Blob([t],{type:i});if(window.navigator.msSaveOrOpenBlob)window.navigator.msSaveOrOpenBlob(n,e);else{var s=document.createElement(\"a\"),o=URL.createObjectURL(n);s.href=o,s.download=e,document.body.appendChild(s),s.click(),setTimeout(function(){document.body.removeChild(s),window.URL.revokeObjectURL(o)},0)}};var bot={version:\"2.0\",botInterval:null,fakeTypeInterval:null,condInterval:null,rate:500,condRate:1e3,isRunning:!1,isAutoNext:!1,isFirstRun:!0,isQueueRunning:!0,isCondsRunning:!0,cp:{btn:\"\",btnAutoNext:\"\",panel:\"\",rateController:\"\",rateText:\"\",listForm:\"\",addToList:\"\",isHidden:!1,position:\"left\",init(){const e=document.querySelector(\"body\"),i=document.querySelector(\"#botPanel\");i&&i.remove();const n=document.querySelector(\"#sortablejs\");n&&n.remove();const s=document.createElement(\"script\");s.id=\"sortablejs\",s.src=\"https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js\",e.appendChild(s);const o=(t,e)=>msg={ifs:[t],thens:[e]};s.addEventListener(\"load\",()=>{Sortable.create(this.list,{group:\"botQueue\",animation:100,onEnd:t=>{const e=this.list.children,i=[];for(let t=0;t<e.length;t++)i.push(e[t].textContent);bot.text.mutateTextArr(i)}}),Sortable.create(this.condList,{group:\"botConds\",animation:100,onEnd:t=>{const e=this.condList.children,i=[];for(let t=0;t<e.length;t++){const n=e[t].children[0].textContent,s=e[t].children[1].textContent,a=o(n,s);i.push(a)}bot.text.mutateTextArr(i)}})}),this.all=document.createElement(\"div\"),this.all.id=\"bot--all-without-hide-btn\";const a=(t,e,i=\"all\",n=\"div\")=>{this[t]=document.createElement(n);for(let i=0;i<e.length;i++)this[t].appendChild(this[e[i]]);this[i].appendChild(this[t])},r=(t,e,i,n,s=!1,o=!1,r)=>{this[e]=document.createElement(\"input\"),this[e].type=\"checkbox\",this[e].checked=s,this[e].disabled=o,this[e].addEventListener(\"change\",t=>{const e=t.target.checked;bot.text[i](e),r&&r(e)}),a(t,[e],\"all\",\"label\"),this[t].appendChild(document.createTextNode(n))},l=(e,i,n,s,o=\"all\")=>{this[e]=document.createElement(\"button\"),t(this[e],null,n),this[e].appendChild(document.createTextNode(i)),this[e].addEventListener(\"click\",s),this[o].appendChild(this[e])};l(\"hideBtn\",\"HIDE\",[\"bot--btn\",\"bot--hide-btn\"],t=>{this.toggleHide()}),this.panel=document.createElement(\"div\"),this.panel.id=\"botPanel\",this.onOffSwitches=document.createElement(\"div\"),this.onOffSwitches.classList.add(\"onOffSwitches\"),l(\"btn\",\"ON/OFF\",[\"bot--btn\",\"bot--switch\"],t=>{bot.toggle()},\"onOffSwitches\"),l(\"queueBtn\",\"Queue\",[\"bot--btn\",\"btn-on\",\"onOffSpecific\"],t=>{bot.onOffSpecific(\"queue\")},\"onOffSwitches\"),l(\"conditsBtn\",\"Condits\",[\"bot--btn\",\"btn-on\",\"onOffSpecific\"],t=>{bot.onOffSpecific(\"conds\")},\"onOffSwitches\"),this.all.appendChild(this.onOffSwitches),r(\"loopDiv\",\"loopBox\",\"setLoop\",\"Loop \",!0),r(\"replyDiv\",\"replyBox\",\"setReply\",\"Reply Mode \",!1,!1,t=>{this.replyAllDiv.classList.toggle(\"unactive\"),this.replyAllBox.disabled=!t}),r(\"replyAllDiv\",\"replyAllBox\",\"setReplyAll\",\"Send whole queue\",!1,!0),t(this.replyAllDiv,null,[\"bot--box-l2\",\"unactive\"]),r(\"randomDiv\",\"randomBox\",\"setRandom\",\"Random\"),r(\"realTypeDiv\",\"realTypeBox\",\"setRealType\",\"Real Type™\"),r(\"fakeTypeDiv\",\"fakeTypeBox\",\"setFakeType\",\"Fake Typing\"),((t,e,i,n,s,o,r,l,d,h,c)=>{this[i]=document.createElement(\"span\"),this[i].innerHTML=n,this[s]=document.createElement(\"input\"),this[s].id=o,this[s].type=\"range\",this[s].min=r,this[s].max=l,this[s].value=d,this[s].step=h,this[s].addEventListener(\"input\",c),a(t,[i,s]),this.rate.id=e})(\"rate\",\"bot--rate\",\"rateText\",\'Send once/<span id=\"bot--rate-gauge\">\'+bot.rate+\"ms</span>\",\"rateController\",\"bot--rate-controller\",0,1e4,bot.rate,1,t=>{let e=t.target.value;bot.changeRate(e)}),setTimeout(()=>this.rateGauge=document.querySelector(\"#bot--rate-gauge\"),0),l(\"btnAutoNext\",\"Auto Next\",[\"bot--btn\",\"bot--auto-next\"],t=>{bot.toggleAutoNext()}),l(\"conditsSwitch\",\"conditionals >\",[\"bot--condits-switch\",\"bot--btn\"],this.handleConditsSwitch.bind(this));const d=(t,e,i,n,s,o)=>{this[t]=document.createElement(\"div\"),this[t].classList.add(...e),this[i]=document.createElement(\"select\");for(let t=0;t<n.length;t++){const e=document.createElement(\"option\");e.appendChild(document.createTextNode(n[t])),e.value=n[t],this[i].appendChild(e)}this[t].appendChild(document.createTextNode(s)),this[t].appendChild(this[i]),this[i].addEventListener(\"change\",o)};a(\"tempCondForm\",[\"conditsSwitch\"]),t(this.tempCondForm,null,[\"bot--container\"]),this.condIfInput=document.createElement(\"input\"),this.condIfInput.placeholder=\"can be RegEx (eg. /regex/)\",this.condIfInput.required=!0,this.condIfLabel=document.createTextNode(\"IF: \"),this.condThenInput=document.createElement(\"input\"),this.condThenInput.required=!0,this.condThenLabel=document.createTextNode(\"THEN: \"),d(\"condTemplates\",[\"bot--cond-templates\"],\"selectCondTemplate\",[\"NONE\",\"fake k/m17\"],\"Template \",t=>{bot.text.setTemplate(t.target.value)}),a(\"condTemplatesDiv\",[\"condTemplates\"]),this.condTemplatesDiv.classList.add(\"templates-modes-div\"),a(\"condIfDiv\",[\"condIfLabel\",\"condIfInput\"]),a(\"condThenDiv\",[\"condThenLabel\",\"condThenInput\"]),l(\"removeCondsBtn\",\"X\",[\"bot--btn\"],t=>{bot.text.removeQueue()}),this.removeCondsBtn.type=\"button\",this.sub=document.createElement(\"input\"),this.sub.type=\"submit\",this.sub.classList.add(\"necessary_submit\"),a(\"condControl\",[\"condIfDiv\",\"condThenDiv\",\"removeCondsBtn\",\"sub\"]),this.condControl.classList.add(\"bot--list-control\"),this.condList=document.createElement(\"div\"),this.condList.classList.add(\"bot--list\"),this.condList.addEventListener(\"click\",t=>{bot.text.removeMessage(t.target.closest(\".bot--queue-item\").dataset.id)}),a(\"condForm\",[\"condTemplatesDiv\",\"condControl\",\"condList\"],\"all\",\"form\"),this.condForm.classList.add(\"cond-form\",\"unactive-form\"),this.condForm.addEventListener(\"submit\",t=>{t.preventDefault();const e=this.condIfInput.value,i=this.condThenInput.value;bot.text.addMessage(o(e,i)),this.condIfInput.value=this.condThenInput.value=\"\"}),this.addToList=document.createElement(\"input\"),this.addToList.placeholder=\"Add to message queue\",this.addToList.setAttribute(\"style\",\"width: 80%\"),l(\"resetQueueBtn\",\"R\",[\"bot--btn\"],t=>{bot.text.reset()}),l(\"removeQueueBtn\",\"X\",[\"bot--btn\"],t=>{bot.text.removeQueue()}),this.removeQueueBtn.id=\"bot--remove-queue\",this.upperDiv=document.createElement(\"div\"),this.upperDiv.classList.add(\"bot--list-control\"),this.upperDiv.appendChild(this.addToList),this.upperDiv.appendChild(this.resetQueueBtn),this.upperDiv.appendChild(this.removeQueueBtn),this.list=document.createElement(\"div\"),this.list.classList.add(\"bot--list\"),this.list.addEventListener(\"click\",t=>{bot.text.removeMessage(t.target.dataset.id)}),d(\"modes\",[\"bot--modes\"],\"selectMode\",[\"NONE\",\"increment\",\"parrot\",\"parrot+\"],\"Mode \",t=>{bot.text.setMode(t.target.value)}),d(\"templates\",[\"bot--templates\"],\"select\",[\"NONE\",\"waves\",\"Bałkanica\"],\"Template \",t=>{bot.text.setTemplate(t.target.value)}),a(\"templatesModesDiv\",[\"modes\",\"templates\"]),this.templatesModesDiv.classList.add(\"templates-modes-div\"),a(\"listForm\",[\"templatesModesDiv\",\"upperDiv\",\"list\"],\"all\",\"form\"),this.listForm.addEventListener(\"submit\",t=>{t.preventDefault();const e=this.addToList.value;bot.text.addMessage(e),this.addToList.value=\"\"});const h=()=>{const t=this.impSeparation.value,e=this.importFile.files,i=this.importInput.value,n=i||e;bot.text.import(t,n)};this.expImp=document.createElement(\"div\"),this.exportDiv=document.createElement(\"div\"),this.importDiv=document.createElement(\"form\"),this.importDiv.addEventListener(\"submit\",t=>{t.preventDefault(),h()}),this.expImp.classList.add(\"bot--expimp\"),l(\"exportBtn\",\"< Export >\",[\"bot--btn\",\"bot--export\"],t=>{const e=this.expName.value;bot.text.export(e)},\"exportDiv\"),l(\"importBtn\",\"> Import <\",[\"bot--btn\",\"bot--import\"],t=>{},\"importDiv\"),this.expName=document.createElement(\"input\"),this.expName.placeholder=\"file name\",this.expName.id=\"bot--expName\",this.impSeparation=document.createElement(\"input\"),this.impSeparation.placeholder=\"sep.\",this.impSeparation.id=\"bot--impSep\",this.importFile=document.createElement(\"input\"),this.importFile.type=\"file\",this.exportDiv.classList.add(\"bot--export-div\"),this.exportDiv.appendChild(this.expName),this.importDiv.classList.add(\"bot--import-div\"),this.importDiv.appendChild(this.impSeparation),this.importDiv.appendChild(this.importFile),this.importInput=document.createElement(\"textarea\"),this.importInput.placeholder=\"Paste or type in some text to import\",this.importDiv.appendChild(this.importInput),this.expImp.appendChild(this.exportDiv),this.expImp.appendChild(this.importDiv),this.all.appendChild(this.expImp),this.panel.appendChild(this.hideBtn),l(\"sideSwitch\",\"<|>\",[\"sideSwitch\",\"bot--btn\"],t=>{this.panel.style.setProperty(\"right\",\"right\"===this.position?\"initial\":0),this.position=\"right\"===this.position?\"left\":\"right\"},\"panel\"),((t,e,i=\"none\",n=\"all\",s=\"div\")=>{this[t]=document.createElement(s),this[t].classList.add(...e);const o=document.createTextNode(i);this[t].appendChild(o),this[n].appendChild(this[t])})(\"title\",[\"bot--title\"],\"Bl🎈🎈nBot v\"+bot.version,\"panel\"),this.panel.appendChild(this.all),e.insertBefore(this.panel,e.firstChild),this.stylize()},handleConditsSwitch(t){this.conditsSwitch.textContent=bot.text.isConditsShown?\"conditionals >\":\"< queue\",e(this.conditsSwitch,\"toggleCondits\"),this.listForm.classList.toggle(\"unactive-form\"),this.condForm.classList.toggle(\"unactive-form\")},toggleHide(){this.isHidden?(this.hideBtn.style.setProperty(\"background\",\"red\"),this.all.style.setProperty(\"display\",\"flex\")):(this.hideBtn.style.setProperty(\"background\",\"green\"),this.all.style.setProperty(\"display\",\"none\")),this.isHidden=!this.isHidden},stylize(){const t=\"\\n                    #botPanel {\\n                        color: white;\\n                        padding: 10px;\\n                        z-index: 1000;\\n                        position: absolute;\\n                        width: 450px;\\n                        background: #0008;\\n                        box-sizing: border-box;\\n                    }\\n\\n                    .sideSwitch {\\n                        margin-left: 10px;\\n                    }\\n\\n                    #botPanel label *, #botPanel label {\\n                        cursor: pointer;\\n                    }\\n\\n                    .bot--title {\\n                        display: inline-block;\\n                        position: absolute;\\n                        right: 10px;\\n                        color: #fff8;\\n                        font-weight: bold;\\n                    }\\n\\n                    #bot--all-without-hide-btn {\\n                        display: flex;\\n                        flex-flow: column;\\n                        justify-content: center;\\n                        margin: 10px 0 0;\\n                    }\\n\\n                    .bot--list {\\n                        max-height: 20vh;\\n                        overflow: auto;\\n                    }\\n\\n                    .bot--container {\\n                        display: flex;\\n                        justify-content: space-between;\\n                        align-items: center;\\n                        margin-top: 10px;\\n                    }\\n\\n                    .bot--queue-item {\\n                        padding: 2px;\\n                        background: #fff9;\\n                        color: black;\\n                        border-top: 1px solid #777;\\n                        max-width: 100%;\\n                        overflow: hidden;\\n                        cursor: pointer;\\n                        position: relative;\\n                        text-overflow: ellipsis;\\n                        white-space: nowrap;\\n                    }\\n\\n                    .bot--list-active-el {\\n                        background: #fffc;\\n                    }\\n\\n                    .bot--list-active-el::after {\\n                        content: \'\';\\n                        position: absolute;\\n                        right: 0;\\n                        top: 0;\\n                        height: 100%;\\n                        width: 25px;\\n                        background-image: url(\\\"data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'64\' height=\'64\' fill=\'%23f55\' viewBox=\'0 0 640 640\' shape-rendering=\'geometricPrecision\' text-rendering=\'geometricPrecision\' image-rendering=\'optimizeQuality\' fill-rule=\'evenodd\' clip-rule=\'evenodd\'%3E%3Cpath d=\'M153.581 320L486.42 640.012V-.012L153.581 320z\'/%3E%3C/svg%3E\\\");\\n                        background-position: left;\\n                    }\\n\\n                    #bot--list-control input, .bot--queue-item {\\n                        font-size: 15px;\\n                    }\\n\\n                    #bot--rate {\\n                        margin: 10px 0;\\n                        color: white;\\n                    }\\n\\n                    #bot--rate-controller {\\n                        cursor: pointer;\\n                        width: 100%;\\n                    }\\n\\n                    #bot--rate-gauge {\\n                        font-weight: bold;\\n                    }\\n\\n                    .onOffSwitches {\\n                        display: flex;\\n                    }\\n\\n                    .onOffSwitches > * {\\n                        flex: 1 0 40px;\\n                    }\\n\\n                    .bot--btn {\\n                        padding: 5px;\\n                        background: red;\\n                        color: white;\\n                        border: 2px solid white;\\n                        cursor: pointer;\\n                        font-weight: bold;\\n                    }\\n\\n                    .bot--switch {\\n                        padding: 10px;\\n                        flex: 3 0 200px;\\n                    }\\n\\n                    .bot--remove-queue {\\n                        padding: 2px 6px;\\n                    }\\n\\n                    .bot--list-control {\\n                        display: flex;\\n                        justify-content: space-between;\\n                        align-items: center;\\n                        margin: 10px 0 5px;\\n                    }\\n\\n                    .bot--expimp {\\n                        margin: 10px 0 5px;\\n                        display: flex;\\n                        justify-content: space-around;\\n                        flex-flow: column;\\n                    }\\n\\n                    .bot--expimp input[type=\'file\']{\\n                        width: 200px;\\n                        margin-left: 10px;\\n                    }\\n\\n                    .bot--expimp input{\\n                        width: 100%;\\n                    }\\n\\n                    .bot--expimp div {\\n                        margin-top: 10px;\\n                    }\\n\\n                    .bot--import {\\n                        background: #8f8;\\n                        margin-top: 10px;\\n                        color: #080;\\n                    }\\n\\n                    .bot--export {\\n                        background: #f88;\\n                        color: #800;\\n                    }\\n\\n                    #bot--impSep {\\n                        width: 25px;\\n                        height: 15px;\\n                    }\\n\\n                    #bot--expName {\\n                        width: 60px;\\n                    }\\n\\n                    textarea {\\n                        width: 100%;\\n                        resize: none;\\n                    }\\n\\n                    .bot--box-l2 {\\n                        margin-left: 20px;\\n                    }\\n\\n                    .bot--box-l3 {\\n                        margin-left: 30px;\\n                    }\\n\\n                    #botPanel label.unactive {\\n                        color: #aaa;\\n                    }\\n\\n                    .bot--condits-switch {\\n                        width: 35%;\\n                        background: #f55 !important;\\n                    }\\n\\n                    #botPanel .btn-on {\\n                        background: green;\\n                    }\\n\\n                    .unactive-form {\\n                        display: none;\\n                    }\\n                    \\n                    .cond-form .bot--list-control {\\n                        font-weight: bold;\\n                    }\\n                    \\n                    .cond-form input {\\n                        width: 100%;\\n                    }\\n\\n                    .bot--cond-item {\\n                        display: flex;\\n                    }\\n\\n                    .bot--cond-item > * {\\n                        width: 50%;\\n                        height: 100%;\\n                        overflow: hidden;\\n                        text-overflow: ellipsis;\\n                        white-space: nowrap;\\n                    }\\n\\n                    .then-part {\\n                        background: #f779;\\n                        padding: 0 3px;\\n                    }\\n\\n                    .necessary_submit {\\n                        display: none;\\n                    }\\n\\n                    .templates-modes-div {\\n                        margin-top: 10px;\\n                        display: flex;\\n                        justify-content: space-between;\\n                    }\\n                \",e=document.createElement(\"style\");e.id=\"botStyle\",e.styleSheet?e.styleSheet.cssText=t:e.appendChild(document.createTextNode(t));const i=document.querySelector(\"#botStyle\");i&&i.remove(),document.getElementsByTagName(\"head\")[0].appendChild(e)}},text:{textArr:[\"🎈\"],initCondArr:[{ifs:[\"m\"],thens:[\"k\"]}],input:\"\",counter:0,oldCounter:0,msgCounter:0,isLoop:!0,isReply:!1,isReplyAll:!1,isRandom:!1,isRealType:!1,isFakeType:!1,fakeTypeRate:300,initialRate:500,itemPause:800,mode:null,msg:\"\",isConditsShown:!1,counters:[\"counter\",\"oldCounter\"],checkCond(){const t=this.getStrangerMsg();if(t){const e=t.trim().toLowerCase();for(let t=0;t<this.condListLength;t++){const i=this.condArr[t];let n=i.ifs[0];const s=i.thens[0];if(/^\\/[\\s\\S]*\\//.test(n)){const t=n.replace(/^\\/|\\/$/g,\"\"),i=new RegExp(t);e.match(i)&&(this.insertMsg(s),bot.sendMsg())}else if(e===(n=n.trim().toLowerCase())){this.insertMsg(s);break}}bot.sendMsg()}},checkCounters(){for(const t of this.counters)this[t]=this[t]+1>this.listLength?0:this[t]},insert(){if(0===this.listLength)bot.stop(),alert(\"Empty queue!\");else{switch(this.checkCounters(),this.isRandom&&!this.afterRandomChecked&&(this.counter=Math.floor(Math.random()*this.listLength)),this.mode){case\"parrot\":this.insertMsg(this.getStrangerMsg());break;case\"parrot+\":{const t=this.textArr[this.counter].split(\"$msg\",2),e=t[0]+this.getStrangerMsg()+(t[1]?t[1]:\"\");this.insertFromQueue(e)}break;case\"increment\":this.initialMsg=this.textArr[0],this.msg+=this.initialMsg,this.insertMsg(this.msg),this.msgCounter++;break;default:this.insertFromQueue(this.textArr[this.counter])}this.isRandom&&(this.afterRandomChecked=!1),this.setActiveListEl()}},setActiveListEl(){this.list.children[this.counter].classList.add(\"bot--list-active-el\"),this.oldCounter!==this.counter&&this.list.children[this.oldCounter].classList.remove(\"bot--list-active-el\"),this.oldCounter=this.counter},insertFromQueue(t){this.insertMsg(t),this.isRandom||this.counter++,this.counter+1>this.listLength&&(this.isRandom||(this.counter=0),this.isLoop||bot.stop())},insertMsg(t){this.input.value=t},getStrangerMsg(){if(bot.isLastMsgStrangers()){return bot.log.lastChild.textContent.replace(/Obcy:\\s/,\"\")}return null},setLoop(t){this.isLoop=t},setReply(t){this.isReply=t},setReplyAll(t){this.isReplyAll=t},setRandom(t){this.isRandom=t,t&&(this.list.children[this.counter].classList.remove(\"bot--list-active-el\"),this.counter=Math.floor(Math.random()*this.listLength),this.list.children[this.counter].classList.add(\"bot--list-active-el\"),this.afterRandomChecked=!0)},setRealType(t){this.isRealType=t,t?bot.changeRate(1500,!1,!0):bot.changeRate(this.initialRate)},setFakeType(t){this.isFakeType=t,t||clearInterval(bot.fakeTypeInterval),bot.isRunning&&bot.start()},toggleCondits(t){this.isConditsShown=!t,this.presentArr=t?\"textArr\":\"condArr\",this.presentList=t?\"list\":\"condList\",this.presentListLength=t?\"listLength\":\"condListLength\",this.updateList()},realTypeSetup(){if(this.isRealType){const t=this.textArr[this.counter].length;bot.changeRate(this.initialRate/10*t+this.itemPause,!0)}},setTemplate(t){if(confirm(\"This will clear the list of messages. Proceed?\")){let e=\"\";if(this.isConditsShown)switch(t){case\"fake k/m17\":e=[{ifs:[\"m\"],thens:[\"k\"]},{ifs:[\"k\"],thens:[\"m\"]},{ifs:[\"/.*lat.*/\"],thens:[\"17\"]},{ifs:[\"/.*m[\\\\d].*/\"],thens:[\"k17\"]},{ifs:[\"/.*k[\\\\d].*/\"],thens:[\"m17\"]}]}else switch(t){case\"waves\":e=[\"🎈\",\"🎈🎈\",\"🎈🎈🎈\",\"🎈🎈🎈🎈\",\"🎈🎈🎈🎈🎈\",\"🎈🎈🎈🎈\",\"🎈🎈🎈\",\"🎈🎈\",\"🎈\"];break;case\"Bałkanica\":e=\"Bałkańska w żyłach płynie krew,| kobiety, wino, taniec, śpiew.| Zasady proste w życiu mam,| nie rób drugiemu tego-| czego ty nie chcesz sam!| Muzyka, przyjaźń, radość, śmiech.| Życie łatwiejsze staje się.| Przynieście dla mnie wina dzban,| potem ruszamy razem w tan.| Będzie! Będzie zabawa!| Będzie się działo!| I znowu nocy będzie mało.| Będzie głośno, będzie radośnie| Znów przetańczymy razem całą noc.| Będzie! Będzie zabawa!| Będzie się działo!| I znowu nocy będzie mało.| Będzie głośno, będzie radośnie| Znów przetańczymy razem całą noc.| Orkiestra nie oszczędza sił| już trochę im brakuje tchu.| Polejcie wina również im| znów na parkiecie będzie dym.| Bałkańskie rytmy, Polska moc!| Znów przetańczymy całą noc.| I jeszcze jeden malutki wina dzban| i znów ruszymy razem w tan!| Będzie! Będzie zabawa!| Będzie się działo!| I znowu nocy będzie mało.| Będzie głośno, będzie radośnie| Znów przetańczymy razem całą noc.| Będzie! Będzie zabawa!| Będzie się działo!| I znowu nocy będzie mało.| Będzie głośno, będzie radośnie| Znów przetańczymy razem całą noc.|\".split(\"|\")}this.mutateTextArr(e)}bot.cp.select.value=\"NONE\"},setMode(t){if(\"parrot\"===t||\"parrot+\"===t){this.mode=\"parrot\"===t?t:\"parrot+\";const e=bot.cp.replyBox;e.checked||e.click()}else this.mode=\"NONE\"!==t?t:null;this.reset()},mutateTextArr(t,e=!1){e?this[e+\"Arr\"]=t:this[this.presentArr]=t,this.updateList()},addMessage(t){if(t){let e=\"\";e=this.isConditsShown?t:t.replace(/\\s/g,\" \");const i=[...this[this.presentArr],e];this.mutateTextArr(i)}},removeMessage(t){t=parseInt(t),this[this.presentArr].splice(t,1),this.isConditsShown||(0!==this.counter&&t!==this.counter&&t<this.counter?this.counter-=1:t===this.counter&&this.reset()),this.updateList()},removeQueue(){confirm(\"This will clear list of messages. Proceed?\")&&this.mutateTextArr(this.isConditsShown?this.initCondArr:[\"🎈\"])},updateList(){if(this.isConditsShown){this.condList.innerHTML=\"\";const t=document.createDocumentFragment();this.condArr.map((e,i)=>{const n=document.createElement(\"div\"),s=document.createElement(\"div\"),o=document.createElement(\"div\");n.dataset.id=i,n.classList.add(\"bot--queue-item\",\"bot--cond-item\"),s.classList.add(\"if-part\"),o.classList.add(\"then-part\"),s.appendChild(document.createTextNode(e.ifs[0])),o.appendChild(document.createTextNode(e.thens[0])),n.appendChild(s),n.appendChild(o),t.appendChild(n)}),this.condList.appendChild(t),this.condListLength=this.condArr.length}else{this.list.innerHTML=\"\";const t=document.createDocumentFragment();this.textArr.map((e,i)=>{if(e&&\" \"!==e&&\"\\n\"!==e){const n=document.createTextNode(e),s=document.createElement(\"div\");s.dataset.id=i,s.appendChild(n),s.classList.add(\"bot--queue-item\"),t.appendChild(s)}else this.textArr.splice(i,0);this.list.appendChild(t)}),this.listLength=this.textArr.length,this.checkCounters(),this.setActiveListEl()}},reset(){this.isConditsShown||(this.listLength&&(this.checkCounters(),this.list.children[this.counter+1>this.listLength?0:this.counter].classList.remove(\"bot--list-active-el\"),this.list.children[0].classList.add(\"bot--list-active-el\")),this.counter=this.oldCounter=this.msgCounter=0,this.msg=\"\")},export(t){const e={settings:{boxes:{isLoop:this.isLoop,isReply:this.isReply,isReplyAll:this.isReplyAll,isRandom:this.isRandom,isRealType:this.isRealType,isFakeType:this.isFakeType},switches:{queue:bot.isQueueRunning,conds:bot.isCondsRunning},rate:bot.rate,mode:this.mode},textArr:this.textArr,condArr:this.condArr};i(JSON.stringify(e),(t||this.textArr[0])+\".json\",\"text/plain\")},import(t,e){if(\"string\"==typeof e)(e=>{\"\\\\n\"===t&&(t=\"\\n\");const i=e.split(t);this.mutateTextArr(i)})(e);else{const t=t=>{const e=t.target.result,i=JSON.parse(e),n=!this.isConditsShown;this.toggleCondits(!0),this.mutateTextArr(i.textArr),this.toggleCondits(!1),this.mutateTextArr(i.condArr),this.toggleCondits(n),!i.settings.switches.queue&&i.settings.switches.conds&&this.isConditsShown;const s=Object.keys(i.settings.boxes),o=Object.values(i.settings.boxes),a=bot.cp;for(let t=0;t<s.length;t++){const e=s[t],i=o[t];if(this[e]!==i){a[e.slice(2,3).toLowerCase()+e.slice(3)+\"Box\"].click()}}bot.changeRate(i.settings.rate,!1,!0),this.setMode(i.settings.mode);const r=i.settings.switches;bot.onOffSpecific(\"queue\",r.queue),bot.onOffSpecific(\"conds\",r.conds)};if(!window.FileReader)return alert(\"Your browser is not supported\"),!1;var i=new FileReader;if(e.length){var n=e[0];i.readAsText(n),i.addEventListener(\"load\",t)}else alert(\"Please upload a file or enter some text before continuing\")}},init(){this.input=bot.inp,this.list=bot.cp.list,this.listLength=this.list.length,this.condList=bot.cp.condList,this.initialRate=bot.rate,this.condArr=this.initCondArr,this.presentArr=\"textArr\",this.presentList=\"list\",this.presentListLength=\"listLength\",this.updateList()}},start(){if(this.stop(),this.cp.btn.style.setProperty(\"background\",\"green\"),this.text.realTypeSetup(),this.botInterval=setInterval(()=>{this.runSetup()},this.rate),this.isQueueRunning&&this.text.isFakeType){let t=1;this.fakeTypeInterval=setInterval(()=>{++t>3&&(t=1);let e=\"Faking typing.\";switch(t){case 2:e+=\".\";break;case 3:e+=\"..\"}this.text.insertMsg(e)},this.text.fakeTypeRate)}this.isRunning=!0},stop(){this.isRunning&&(this.cp.btn.style.setProperty(\"background\",\"red\"),clearInterval(this.botInterval),clearInterval(this.fakeTypeInterval),this.botInterval=0,this.fakeTypeInterval=0,this.isRunning=!1)},isLastMsgStrangers(){const t=this.log.lastChild;return!!t&&t.classList.contains(this.strangerMsgClass)},runSetup(){if(this.isCondsRunning&&this.text.checkCond(),this.isQueueRunning){if(this.text.isReply)try{(this.isLastMsgStrangers()||this.text.isReplyAll&&this.text.counter>0)&&(this.text.insert(),this.sendMsg())}catch(t){}else this.text.insert(),this.sendMsg();this.isFirstRun=!1,this.text.isRealType&&this.start()}},sendMsg(){this.btn.click();const t=document.querySelector(\".sd-interface button\");t&&t.click()},leaveIfDisconnected(){this.btn.classList.contains(\"disabled\")&&this.isAutoNext&&(this.btnEsc.click(),this.text.reset())},toggle(){this.isRunning?this.stop():(this.runSetup(),this.start(),this.isFirstRun=!0)},changeRate(t,e=!1,i=!1){if(this.rate=t,!e){this.text.initialRate=t;const e=this.rate<1e3?Math.floor(this.rate)+\"ms\":(this.rate/1e3).toFixed(1)+\"s\";this.cp.rateGauge.textContent=e}i&&(this.cp.rateController.value=t),this.isRunning&&this.start()},toggleAutoNext(){this.isAutoNext?this.cp.btnAutoNext.style.setProperty(\"background\",\"red\"):this.cp.btnAutoNext.style.setProperty(\"background\",\"green\"),this.isAutoNext=!this.isAutoNext},onOffSpecific(t=\"queue\",e=null){const i=\"queue\"===t?\"queueBtn\":\"conditsBtn\",n=\"queue\"===t?\"isQueueRunning\":\"isCondsRunning\",s=\"queue\"!==t?\"isQueueRunning\":\"isCondsRunning\";e!==this[n]&&(this.cp[i].classList.toggle(\"btn-on\"),this[n]=!this[n],this.isRunning&&this.start()),this[s]!==this[n]&&(\"queue\"===t?this[n]===this.text.isConditsShown&&this.cp.handleConditsSwitch():this[n]===!this.text.isConditsShown&&this.cp.handleConditsSwitch())},init(t,e=null,i=null,n=null,s=null){this.btn=e?document.querySelector(e):null,this.btnEsc=i?document.querySelector(i):null,this.inp=t?document.querySelector(t):null,this.log=n?document.querySelector(n):null,this.strangerMsgClass=s,setInterval(()=>{this.isRunning&&this.leaveIfDisconnected()},1e3),this.cp.init(),this.text.init()}};window.bot=bot}bot.init(\"#box-interface-input\",\"button.o-any.o-send\",\"button.o-any.o-esc\",\"#log-dynamic\",\"log-stranger\");'

website = '6obcy'
url = ''
msgWindowsEnabled = True

window = tkinter.Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
def messageWindow(type, title, msg):
    if(msgWindowsEnabled):
        if type == 'error':
            messagebox.showerror(title, msg)
        elif type == 'warning':
            messagebox.showwarning(title, msg)
        else:
            messagebox.showinfo(title, msg)
    

sites = {
    '6obcy': 'https://6obcy.org/rozmowa',
    'e-chat.co': 'echaturl',
    'test': 'https://6obcy.org'
}
siteUrl = sites.get(website, None)

firefoxFound = True
browserLoadWait = 5

if siteUrl is None:
    messageWindow('error', 'BloonBot launcher', 'No such website available')
else:
    messageWindow('warning' ,'BloonBot launcher', 'Bot installation works best on Firefox. Do not use your mouse after you confirm this window. Installing will take about 10 seconds.')

    try:
        subprocess.call([r'C:\Program Files\Mozilla Firefox\firefox.exe', '-new-tab', siteUrl])
    except:
        webbrowser.open_new(siteUrl)
        firefoxFound = False
        browserLoadWait = 10
        
    time.sleep(browserLoadWait)
    pyautogui.click(500, 400)

    keyb = Controller()

    with keyb.pressed(Key.ctrl):
        with keyb.pressed(Key.shift):
            if firefoxFound: consoleKey = 'k'
            else: consoleKey = 'j'

            keyb.press(consoleKey)
            keyb.release(consoleKey)

    pyperclip.copy(botCode)
    time.sleep(1.5)
    keyb.press(Key.ctrl)
    keyb.press('v')
    time.sleep(0.1)
    keyb.release(Key.ctrl)
    keyb.release('v')

    time.sleep(0.1)
    keyb.press(Key.enter)
    time.sleep(0.1)
    keyb.release(Key.enter)

    time.sleep(1)
    keyb.press(Key.f12)
    time.sleep(0.2)
    keyb.release(Key.f12)
    if firefoxFound:
        messageWindow('info', 'BloonBot launcher', 'BloonBot has been installed. You can safely use your mouse now.')
    else:
        messageWindow('warning', 'BloonBot launcher', 'Firefox not found. If bot is not correctly installed install Firefox and try again.')

window.deiconify()
window.destroy()
window.quit()