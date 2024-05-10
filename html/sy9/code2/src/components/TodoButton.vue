<template>
    <div class="button-container mt-3">
        <div class="btn-group">
            <button type="button" class="btn" :class="active === 0 ? 'btn-primary' : 'btn-secondary'">全部
            </button>
            <button type="button" class="btn" :class="active === 1 ? 'btn-primary' : 'btn-secondary'">已完成
            </button>
            <button type="button" class="btn" :class="active === 2 ? 'btn-primary' : 'btn-secondary'">未完成
            </button>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const active = ref(0)
const emit = defineEmits(['updateActive'])
const btnClick=(index)=>{
    active.value=index
    emit('updateActive',index)
}
</script>
<style scoped>
.button-container {
    width: 700px;
    text-align: center;
}
</style>