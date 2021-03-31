<template>
    <div>
        <p>{{ session.jump_rope_number }}</p>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "Session",
    data () {
        return {
            session: {}
        }
    },
    mounted() {
        this.getSession()
    },
    methods: {
        getSession() {
            const sessionID = this.$route.params.id
            
            axios
                .get(`/api/v1/sessions/${sessionID}/`)
                .then(response => {
                    this.session = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>