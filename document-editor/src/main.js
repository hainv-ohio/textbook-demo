import { createApp } from "vue";
import { createPinia } from "pinia";
import CKEditor from "@ckeditor/ckeditor5-vue";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

app.use(CKEditor);
app.use(createPinia());
app.use(router);

app.mount("#app");
