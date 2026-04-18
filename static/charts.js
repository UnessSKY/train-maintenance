const charts = {};

function createChart(id, label) {
    const ctx = document.getElementById(id).getContext("2d");
    return new Chart(ctx, {
        type: "line",
        data: { labels: [], datasets: [{ label: label, data: [] }] },
        options: { animation: false }
    });
}

charts.vibration = createChart("vibrationChart", "Vibration");
charts.temperature = createChart("temperatureChart", "Temperature");
charts.brake_pressure = createChart("brakeChart", "Brake Pressure");
charts.motor_current = createChart("motorChart", "Motor Current");
charts.wheel_rpm = createChart("rpmChart", "Wheel RPM");

async function update() {
    const res = await fetch("/stream");
    const data = await res.json();

    document.getElementById("failure").innerText =
        data.alert ? data.alert.failure_probability : "Training...";
    document.getElementById("rul").innerText =
        data.alert ? data.alert.rul_seconds + " seconds" : "Training...";

    if (data.alert) {
        const box = document.getElementById("alertBox");
        box.innerText = `[${data.alert.severity}] ${data.alert.action}`;
        box.style.color = data.alert.severity === "CRITICAL" ? "red" :
                          data.alert.severity === "WARNING" ? "orange" : "blue";
    }

    for (const s in charts) {
        const chart = charts[s];
        const latest = data.sensors[s].slice(-1)[0];

        chart.data.labels.push(latest.timestamp);
        chart.data.datasets[0].data.push(latest.value);

        if (chart.data.labels.length > 100) {
            chart.data.labels.shift();
            chart.data.datasets[0].data.shift();
        }

        chart.update();
    }
}

setInterval(update, 1000);
