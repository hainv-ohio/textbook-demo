<template>
  <div class="greetings" style="margin: 40px">
    <h1 class="green">{{ msg }}</h1>
    <h3>Enter .pdf document URL for editing!</h3>
    <input style="width: 600px" v-model="docUrl" />
    <button @click="submitUrl">Submit</button>
    <div>{{ status }}</div>
    <div
      style="
        height: 1080px;
        width: 720px;
        margin-top: 40px;
        box-sizing: border-box;
      "
    >
      <ckeditor
        :editor="editor"
        v-model="editorData"
        :config="editorConfig"
      ></ckeditor>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

const editor = ClassicEditor;
const editorConfig = {
//   toolbarGroups: [
//     { name: "document", groups: ["mode", "document", "doctools"] },
//     { name: "clipboard", groups: ["clipboard", "undo"] },
//     {
//       name: "editing",
//       groups: ["find", "selection", "spellchecker", "editing"],
//     },
//     { name: "forms", groups: ["forms"] },
//     { name: "basicstyles", groups: ["basicstyles", "cleanup"] },
//     {
//       name: "paragraph",
//       groups: ["list", "indent", "blocks", "align", "bidi", "paragraph"],
//     },
//     { name: "links", groups: ["links"] },
//     { name: "insert", groups: ["insert"] },
//     { name: "styles", groups: ["styles"] },
//     { name: "colors", groups: ["colors"] },
//     { name: "tools", groups: ["tools"] },
//     { name: "others", groups: ["others"] },
//     { name: "about", groups: ["about"] },
//   ],
//   removeButtons:
//     "NewPage,Print,Save,Templates,Replace,Find,SelectAll,Scayt,Form,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,CreateDiv,Anchor,Flash,Smiley,PageBreak,ShowBlocks,About,Language,Iframe,Image",
};

let docUrl = "";
const editorData = ref("<p>Enter URL first</p>");
const status = ref("");

async function _fetch_doc_api() {
  status.value = "Loading...";
  try {
    const apiUrl = "http://localhost:8000/convert/pdf-to-html";
    const result = await axios.get(apiUrl, {
      params: { filename: encodeURI(docUrl) },
    });
    console.log("result", result);
    editorData.value = result.data;
    status.value = "";
  } catch (e) {
    status.value = `Error: ${e}`;
  }
}

function submitUrl(event) {
  if (event) {
    console.log("event", docUrl);
    _fetch_doc_api();
  }
}
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
