import Vue from 'vue';
import App from './App.vue';
import Dict from './components/dict/Index.vue';

Vue.config.productionTip = true;

const routes = {
    '/': App,
    '/dict': Dict
}

new Vue({
    
    render: h => {
        return h(routes[window.location.pathname]);
    },
    
    created: function () {
        console.log(this.currentRoute)
    }
}).$mount('#app');
