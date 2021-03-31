<template>
    <div>
        <h1>Dashboard</h1>
        <Camera />
    </div>
</template>

<script>
import Camera from "./Camera.vue"

export default {
    name: 'Dashboard',
    components: {
        Camera
    }
}
</script>