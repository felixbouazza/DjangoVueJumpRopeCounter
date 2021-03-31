<template>
    <div>
        <h1>Sessions Page</h1>
        <div 
            v-for="session in sessions"
            v-bind:key="session.id"
        >
            <div>
                <p>Session : {{ session.jump_rope_number }} sauts</p>
                <router-link :to='{ name:"Session", params: { id: session.id }}'>Détails</router-link>
            </div>
        </div>
    </div>

</template>

<script>
import axios from "axios"

export default {
    name: "Sessions",
    data() {
        return {
            sessions: []
        }
    },
    mounted() {
        this.getSessions()
    },
    methods: {
        getSessions() {
            axios
                .get('/api/v1/sessions/')
                .then(response => {
                    this.sessions = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }

}
</script>