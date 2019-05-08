<template>
    <li>
        <h3>{{getData.title}}</h3>
        <p>{{getData.content}}</p>
    </li>
</template>
<script>
export default {
    name:'Vnote',
    data(){
        return{}
    },
    props:{
        data:Object,
    },
    computed:{
        getData(){
            return this.data;
        }
    }
}
</script>
<style>

</style>
