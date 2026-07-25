let cargas = [];
let paros = [];
let audioCtx = null;

// Registrar Service Worker para PWA
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js');
}

// Generador de Efectos de Sonido Estilo Anime/DBZ
function playSound(type) {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    if (type === 'start') {
        // Sonido de Carga de Ki / Inicio
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(120, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(800, audioCtx.currentTime + 0.8);
        gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.8);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.8);
    } else if (type === 'add') {
        // Sonido de Teleport / Instant Transmission
        osc.type = 'sine';
        osc.frequency.setValueAtTime(300, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(1200, audioCtx.currentTime + 0.2);
        gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.2);
    }
}

function iniciarApp() {
    playSound('start');
    const splash = document.getElementById('splash-screen');
    splash.style.opacity = '0';
    setTimeout(() => {
        splash.style.display = 'none';
        document.getElementById('main-app').style.display = 'block';
    }, 500);
}

document.getElementById('formCarga').addEventListener('submit', (e) => {
    e.preventDefault();
    playSound('add');
    const meta = parseFloat(document.getElementById('metaDz').value);
    const hechas = parseFloat(document.getElementById('hechasDz').value);
    
    cargas.push({ id: cargas.length + 1, meta, hechas });
    calcularTodo();
    document.getElementById('hechasDz').value = "0";
});

document.getElementById('formParo').addEventListener('submit', (e) => {
    e.preventDefault();
    playSound('add');
    const hIni = document.getElementById('hInicio').value;
    const hFin = document.getElementById('hFin').value;
    const tipo = document.getElementById('tipoParo').value;

    const [h1, m1] = hIni.split(':').map(Number);
    const [h2, m2] = hFin.split(':').map(Number);
    const duracion = (h2 * 60 + m2) - (h1 * 60 + m1);

    if (duracion > 0) {
        paros.push({ hIni, hFin, duracion, tipo });
        calcularTodo();
    } else {
        alert("La hora de fin debe ser posterior a la hora de inicio.");
    }
});

function calcularTodo() {
    if (cargas.length === 0) return;

    const totalMetas = cargas.reduce((acc, c) => acc + c.meta, 0);
    const totalHechas = cargas.reduce((acc, c) => acc + c.hechas, 0);
    const numCargas = cargas.length;
    const metaPromedioBase = totalMetas / numCargas;

    // Eficiencia ON
    const efOn = metaPromedioBase > 0 ? (totalHechas / metaPromedioBase) * 100 : 0;

    // Calculo paros OFF (Jornada 11h)
    const minParosTotal = paros.reduce((acc, p) => acc + p.duracion, 0);
    const horasParo = minParosTotal / 60;
    const docenasPorHora = metaPromedioBase / 11;
    const docenasDescontadas = horasParo * docenasPorHora;
    const metaFinalOff = Math.max(0, metaPromedioBase - docenasDescontadas);

    // Eficiencia OFF
    const efOff = metaFinalOff > 0 ? (totalHechas / metaFinalOff) * 100 : 0;

    // Métricas en Pantalla
    document.getElementById('mBase').textContent = `${metaPromedioBase.toFixed(1)} dz`;
    document.getElementById('mHechas').textContent = `${totalHechas.toFixed(1)} dz`;
    document.getElementById('eOn').textContent = `${efOn.toFixed(2)}%`;
    document.getElementById('eOff').textContent = `${efOff.toFixed(2)}%`;

    // Render Tabla Cargas
    const tbodyCargas = document.querySelector('#tablaCargas tbody');
    tbodyCargas.innerHTML = '';
    
    cargas.forEach((c) => {
        const efInd = c.meta > 0 ? ((c.hechas / c.meta) * 100).toFixed(1) : 0;
        const factorEf = efOff > 0 ? efOff / 100 : 1;
        const horasTeoricas = ((c.meta / metaPromedioBase) * 11) / factorEf;

        tbodyCargas.innerHTML += `
            <tr>
                <td><b>Carga ${c.id}</b></td>
                <td>${c.meta}</td>
                <td>${c.hechas}</td>
                <td><span class="badge">${efInd}%</span></td>
                <td>${horasTeoricas.toFixed(2)} hrs (${Math.round(horasTeoricas * 60)} min)</td>
            </tr>
        `;
    });

    // Render Tabla Paros
    const tbodyParos = document.querySelector('#tablaParos tbody');
    tbodyParos.innerHTML = '';
    paros.forEach(p => {
        tbodyParos.innerHTML += `
            <tr>
                <td>${p.hIni} - ${p.hFin}</td>
                <td>${p.duracion} min</td>
                <td>${p.tipo === 'fuera' ? 'Fuera de Tiempo' : 'Dentro de Tiempo'}</td>
            </tr>
        `;
    });
}
