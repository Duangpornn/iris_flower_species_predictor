<!DOCTYPE html>
<html lang="th" class="h-full bg-pink-50">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iris Flower Species Predictor - Pink Edition</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        pinkBg: '#fff1f2',
                        sidebarBg: '#ffffff',
                        cardBg: '#ffffff',
                        accentPink: '#ec4899',
                        accentPinkHover: '#db2777',
                        softRose: '#f43f5e'
                    }
                }
            }
        }
    </script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Google Fonts: Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        /* Custom sleek scrollbar for pink theme */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #fff1f2;
        }
        ::-webkit-scrollbar-thumb {
            background: #fbcfe8;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #f472b6;
        }
    </style>
</head>
<body class="h-full bg-pink-50 text-slate-800 flex flex-col md:flex-row antialiased overflow-x-hidden">

    <!-- Left Sidebar: Settings & Inputs -->
    <aside class="w-full md:w-80 bg-white border-r border-pink-100 flex flex-col z-20 shrink-0 h-auto md:h-full shadow-lg">
        <!-- Sidebar Header -->
        <div class="p-5 border-b border-pink-100 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="bg-pink-100 p-2 rounded-xl text-pink-600 shadow-sm">
                    <i class="fa-solid fa-sliders text-base"></i>
                </div>
                <div>
                    <h2 class="font-bold text-sm text-slate-800 tracking-wide">Settings & Inputs</h2>
                    <p class="text-xs text-slate-500">Tune the measurements</p>
                </div>
            </div>
            <button onclick="resetSliders()" class="text-slate-400 hover:text-pink-600 text-xs bg-pink-50 hover:bg-pink-100 p-2 rounded-lg transition" title="Reset values">
                <i class="fa-solid fa-rotate-right"></i>
            </button>
        </div>

        <!-- Sliders Container -->
        <div class="p-6 space-y-6 flex-1 overflow-y-auto">
            <p class="text-xs text-slate-500 leading-relaxed">Adjust the flower measurements below to test the ML classifier model in real-time.</p>
            
            <div class="space-y-6 pt-2">
                <!-- Slider 1: Sepal Length -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="font-medium text-slate-700">Sepal Length</span>
                        <span id="val-sl" class="font-bold text-pink-600 bg-pink-50 px-2.5 py-0.5 rounded-full border border-pink-200 shadow-sm">5.0 cm</span>
                    </div>
                    <input type="range" id="input-sl" min="4.0" max="8.0" step="0.1" value="5.0" oninput="onSliderChange()" class="w-full accent-pink-500 bg-pink-100 rounded-lg h-2 cursor-pointer">
                    <div class="flex justify-between text-[10px] text-slate-400">
                        <span>4.0 cm</span>
                        <span>8.0 cm</span>
                    </div>
                </div>

                <!-- Slider 2: Sepal Width -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="font-medium text-slate-700">Sepal Width</span>
                        <span id="val-sw" class="font-bold text-pink-600 bg-pink-50 px-2.5 py-0.5 rounded-full border border-pink-200 shadow-sm">3.5 cm</span>
                    </div>
                    <input type="range" id="input-sw" min="2.0" max="4.5" step="0.1" value="3.5" oninput="onSliderChange()" class="w-full accent-pink-500 bg-pink-100 rounded-lg h-2 cursor-pointer">
                    <div class="flex justify-between text-[10px] text-slate-400">
                        <span>2.0 cm</span>
                        <span>4.5 cm</span>
                    </div>
                </div>

                <!-- Slider 3: Petal Length -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="font-medium text-slate-700">Petal Length</span>
                        <span id="val-pl" class="font-bold text-pink-600 bg-pink-50 px-2.5 py-0.5 rounded-full border border-pink-200 shadow-sm">3.1 cm</span>
                    </div>
                    <input type="range" id="input-pl" min="1.0" max="7.0" step="0.1" value="3.1" oninput="onSliderChange()" class="w-full accent-pink-500 bg-pink-100 rounded-lg h-2 cursor-pointer">
                    <div class="flex justify-between text-[10px] text-slate-400">
                        <span>1.0 cm</span>
                        <span>7.0 cm</span>
                    </div>
                </div>

                <!-- Slider 4: Petal Width -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="font-medium text-slate-700">Petal Width</span>
                        <span id="val-pw" class="font-bold text-pink-600 bg-pink-50 px-2.5 py-0.5 rounded-full border border-pink-200 shadow-sm">0.6 cm</span>
                    </div>
                    <input type="range" id="input-pw" min="0.1" max="2.5" step="0.1" value="0.6" oninput="onSliderChange()" class="w-full accent-pink-500 bg-pink-100 rounded-lg h-2 cursor-pointer">
                    <div class="flex justify-between text-[10px] text-slate-400">
                        <span>0.1 cm</span>
                        <span>2.5 cm</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sidebar Footer -->
        <div class="p-4 border-t border-pink-100 bg-pink-50/50 text-xs text-slate-500 flex items-center justify-between">
            <span class="font-medium text-slate-600">Model: KNN (k=5)</span>
            <button onclick="randomizeSample()" class="text-pink-600 hover:text-pink-700 font-semibold transition flex items-center gap-1.5">
                <i class="fa-solid fa-dice"></i> Random Sample
            </button>
        </div>
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 flex flex-col h-full overflow-y-auto">
        <!-- Top Navigation Bar -->
        <header class="bg-white/80 border-b border-pink-100 px-6 py-4 flex items-center justify-between sticky top-0 z-10 backdrop-blur-md shadow-sm">
            <div class="flex items-center space-x-3">
                <span class="w-2.5 h-2.5 rounded-full bg-pink-500 animate-pulse"></span>
                <span class="text-xs font-bold uppercase tracking-wider text-pink-600">Iris Species Classification Lab</span>
            </div>
            <div class="flex items-center space-x-3">
                <span class="text-xs bg-pink-50 text-pink-700 px-3 py-1.5 rounded-xl border border-pink-200 font-semibold flex items-center gap-2 shadow-sm">
                    <i class="fa-brands fa-python text-pink-500"></i> scikit-learn
                </span>
                <button onclick="triggerDeployModal()" class="bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white text-xs font-semibold px-4 py-2 rounded-xl shadow-md transition flex items-center gap-1.5">
                    <i class="fa-solid fa-rocket"></i> Deploy
                </button>
            </div>
        </header>

        <!-- Main Dashboard View -->
        <div class="p-6 md:p-8 space-y-8 max-w-7xl mx-auto w-full flex-1">
            
            <!-- Page Title Section -->
            <div>
                <h1 class="text-2xl md:text-3xl font-extrabold text-slate-800 tracking-tight flex items-center gap-2.5">
                    Iris Flower Species Predictor <span class="text-xl">🌸</span>
                </h1>
                <p class="text-xs md:text-sm text-slate-500 mt-1">An interactive ML dashboard to predict and compare flower dimensions in a vibrant pink pastel theme.</p>
            </div>

            <!-- Two-Column Grid: Prediction Result & Comparison Chart -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Left Column: Prediction Results & Probability Bars -->
                <div class="lg:col-span-6 space-y-6">
                    
                    <!-- Prediction Card Container -->
                    <div class="bg-white border border-pink-100 p-6 rounded-3xl shadow-xl flex flex-col justify-between relative overflow-hidden">
                        <!-- Decorative background glow -->
                        <div class="absolute -right-10 -top-10 w-40 h-40 bg-pink-200/50 rounded-full blur-2xl pointer-events-none"></div>

                        <div class="flex items-center justify-between mb-4">
                            <span class="text-xs font-bold uppercase tracking-wider text-pink-600 flex items-center gap-2">
                                <i class="fa-solid fa-bullseye text-sm"></i> Prediction Result
                            </span>
                            <span class="text-[10px] bg-pink-50 text-pink-600 px-2.5 py-1 rounded-lg border border-pink-200 font-medium">KNN Classifier</span>
                        </div>

                        <!-- Big Result Box -->
                        <div class="bg-gradient-to-r from-pink-500 via-rose-500 to-pink-600 p-6 rounded-2xl text-center shadow-lg my-2 border border-pink-300/30 text-white">
                            <p class="text-xs uppercase tracking-widest text-pink-100 font-bold mb-1">Predicted Species</p>
                            <h2 id="pred-species" class="text-3xl md:text-4xl font-black tracking-tight drop-shadow-sm">Setosa</h2>
                            <div class="mt-2 inline-flex items-center gap-1.5 bg-black/15 px-3 py-1 rounded-full text-xs font-bold text-pink-50 shadow-inner">
                                <i class="fa-solid fa-circle-check text-white"></i> Confidence: <span id="pred-confidence">58.0%</span>
                            </div>
                        </div>

                        <!-- Model Probability by Class -->
                        <div class="mt-6 space-y-4">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-700">Model Probability by Class</h3>
                            
                            <!-- Class 0: Setosa -->
                            <div class="space-y-1">
                                <div class="flex justify-between text-xs font-medium">
                                    <span class="text-slate-600 font-medium">Setosa</span>
                                    <span id="prob-val-0" class="text-pink-600 font-bold">58.0%</span>
                                </div>
                                <div class="w-full bg-pink-50 h-3 rounded-full overflow-hidden p-0.5 border border-pink-200 shadow-inner">
                                    <div id="prob-bar-0" class="bg-gradient-to-r from-pink-500 to-rose-500 h-full rounded-full transition-all duration-300" style="width: 58%"></div>
                                </div>
                            </div>

                            <!-- Class 1: Versicolor -->
                            <div class="space-y-1">
                                <div class="flex justify-between text-xs font-medium">
                                    <span class="text-slate-600 font-medium">Versicolor</span>
                                    <span id="prob-val-1" class="text-rose-500 font-bold">41.0%</span>
                                </div>
                                <div class="w-full bg-pink-50 h-3 rounded-full overflow-hidden p-0.5 border border-pink-200 shadow-inner">
                                    <div id="prob-bar-1" class="bg-gradient-to-r from-rose-400 to-pink-400 h-full rounded-full transition-all duration-300" style="width: 41%"></div>
                                </div>
                            </div>

                            <!-- Class 2: Virginica -->
                            <div class="space-y-1">
                                <div class="flex justify-between text-xs font-medium">
                                    <span class="text-slate-600 font-medium">Virginica</span>
                                    <span id="prob-val-2" class="text-purple-500 font-bold">1.0%</span>
                                </div>
                                <div class="w-full bg-pink-50 h-3 rounded-full overflow-hidden p-0.5 border border-pink-200 shadow-inner">
                                    <div id="prob-bar-2" class="bg-gradient-to-r from-purple-400 to-pink-400 h-full rounded-full transition-all duration-300" style="width: 1%"></div>
                                </div>
                            </div>
                        </div>

                        <!-- X-axis scale labels equivalent -->
                        <div class="flex justify-between text-[10px] text-slate-400 pt-2 border-t border-pink-100 mt-4">
                            <span>0</span>
                            <span>20</span>
                            <span>40</span>
                            <span>60</span>
                            <span>80</span>
                            <span>100</span>
                        </div>
                    </div>

                </div>

                <!-- Right Column: Your Inputs vs Dataset Mean Chart -->
                <div class="lg:col-span-6 bg-white border border-pink-100 p-6 rounded-3xl shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-sm font-bold uppercase tracking-wider text-slate-800 flex items-center gap-2">
                                <i class="fa-solid fa-chart-column text-pink-500"></i> Your Inputs vs Dataset Mean
                            </h3>
                            <div class="flex items-center gap-3 text-xs">
                                <div class="flex items-center gap-1.5">
                                    <span class="w-3 h-3 rounded-md bg-pink-500 inline-block shadow-sm"></span>
                                    <span class="text-slate-600 font-medium">Your Values</span>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="w-3 h-3 rounded-md bg-rose-200 inline-block"></span>
                                    <span class="text-slate-600 font-medium">Dataset Average</span>
                                </div>
                            </div>
                        </div>
                        <p class="text-xs text-slate-500 mb-6">Comparison of your configured flower dimensions against the overall Iris dataset mean.</p>
                    </div>

                    <!-- Chart Canvas Container -->
                    <div class="relative w-full h-[280px] md:h-[320px]">
                        <canvas id="comparisonChart"></canvas>
                    </div>
                </div>

            </div>

        </div>

    </main>

    <script>
        // Full 150 standard Iris dataset records matching sklearn.datasets.load_iris()
        const rawIrisData = [
            [5.1, 3.5, 1.4, 0.2, 0], [4.9, 3.0, 1.4, 0.2, 0], [4.7, 3.2, 1.3, 0.2, 0], [4.6, 3.1, 1.5, 0.2, 0], [5.0, 3.6, 1.4, 0.2, 0],
            [5.4, 3.9, 1.7, 0.4, 0], [4.6, 3.4, 1.4, 0.3, 0], [5.0, 3.4, 1.5, 0.2, 0], [4.4, 2.9, 1.4, 0.2, 0], [4.9, 3.1, 1.5, 0.1, 0],
            [5.4, 3.7, 1.5, 0.2, 0], [4.8, 3.4, 1.6, 0.2, 0], [4.8, 3.0, 1.4, 0.1, 0], [4.3, 3.0, 1.1, 0.1, 0], [5.8, 4.0, 1.2, 0.2, 0],
            [5.7, 4.4, 1.5, 0.4, 0], [5.4, 3.9, 1.3, 0.4, 0], [5.1, 3.5, 1.4, 0.3, 0], [5.7, 3.8, 1.7, 0.3, 0], [5.1, 3.8, 1.5, 0.3, 0],
            [5.4, 3.4, 1.7, 0.2, 0], [5.1, 3.7, 1.5, 0.4, 0], [4.6, 3.6, 1.0, 0.2, 0], [5.1, 3.3, 1.7, 0.5, 0], [4.8, 3.4, 1.9, 0.2, 0],
            [5.0, 3.0, 1.6, 0.2, 0], [5.0, 3.4, 1.6, 0.4, 0], [5.2, 3.5, 1.5, 0.2, 0], [5.2, 3.4, 1.4, 0.2, 0], [4.7, 3.2, 1.6, 0.2, 0],
            [4.8, 3.1, 1.6, 0.2, 0], [5.4, 3.4, 1.5, 0.4, 0], [5.2, 4.1, 1.5, 0.1, 0], [5.5, 4.2, 1.4, 0.2, 0], [4.9, 3.1, 1.5, 0.2, 0],
            [5.0, 3.2, 1.2, 0.2, 0], [5.5, 3.5, 1.3, 0.2, 0], [4.9, 3.6, 1.4, 0.1, 0], [4.4, 3.0, 1.3, 0.2, 0], [5.1, 3.4, 1.5, 0.2, 0],
            [5.0, 3.5, 1.3, 0.3, 0], [4.5, 2.3, 1.3, 0.3, 0], [4.4, 3.2, 1.3, 0.2, 0], [5.0, 3.5, 1.6, 0.6, 0], [5.1, 3.8, 1.9, 0.4, 0],
            [4.8, 3.0, 1.4, 0.3, 0], [5.1, 3.8, 1.6, 0.2, 0], [4.6, 3.2, 1.4, 0.2, 0], [5.3, 3.7, 1.5, 0.2, 0], [5.0, 3.3, 1.4, 0.2, 0],
            // Versicolor (50-99)
            [7.0, 3.2, 4.7, 1.4, 1], [6.4, 3.2, 4.5, 1.5, 1], [6.9, 3.1, 4.9, 1.5, 1], [5.5, 2.3, 4.0, 1.3, 1], [6.5, 2.8, 4.6, 1.5, 1],
            [5.7, 2.8, 4.5, 1.3, 1], [6.3, 3.3, 4.7, 1.6, 1], [4.9, 2.4, 3.3, 1.0, 1], [6.6, 2.9, 4.6, 1.3, 1], [5.2, 2.7, 3.9, 1.4, 1],
            [5.0, 2.0, 3.5, 1.0, 1], [5.9, 3.0, 4.2, 1.5, 1], [6.0, 2.2, 4.0, 1.0, 1], [6.1, 2.9, 4.7, 1.4, 1], [5.6, 2.9, 3.6, 1.3, 1],
            [6.7, 3.1, 4.4, 1.4, 1], [5.6, 3.0, 4.5, 1.5, 1], [5.8, 2.7, 4.1, 1.0, 1], [6.2, 2.2, 4.5, 1.5, 1], [5.6, 2.5, 3.9, 1.1, 1],
            [5.9, 3.2, 4.8, 1.8, 1], [6.1, 2.8, 4.0, 1.3, 1], [6.3, 2.5, 4.9, 1.5, 1], [6.1, 2.8, 4.7, 1.2, 1], [6.4, 2.9, 4.3, 1.3, 1],
            [6.6, 3.0, 4.4, 1.4, 1], [6.8, 2.8, 4.8, 1.4, 1], [6.7, 3.0, 5.0, 1.7, 1], [6.0, 2.9, 4.5, 1.5, 1], [5.7, 2.6, 3.5, 1.0, 1],
            [5.5, 2.4, 3.8, 1.1, 1], [5.5, 2.4, 3.7, 1.0, 1], [5.8, 2.7, 3.9, 1.2, 1], [6.0, 2.7, 5.1, 1.6, 1], [5.4, 3.0, 4.5, 1.5, 1],
            [6.0, 3.4, 4.5, 1.6, 1], [6.7, 3.1, 4.7, 1.5, 1], [6.3, 2.3, 4.4, 1.3, 1], [5.6, 3.0, 4.1, 1.3, 1], [5.5, 2.5, 4.0, 1.3, 1],
            [5.5, 2.6, 4.4, 1.2, 1], [6.1, 3.0, 4.6, 1.4, 1], [5.8, 2.6, 4.0, 1.2, 1], [5.0, 2.3, 3.3, 1.0, 1], [5.6, 2.7, 4.2, 1.3, 1],
            [5.7, 3.0, 4.2, 1.2, 1], [5.7, 2.9, 4.2, 1.3, 1], [6.2, 2.9, 4.3, 1.3, 1], [5.1, 2.5, 3.0, 1.1, 1], [5.7, 2.8, 4.1, 1.3, 1],
            // Virginica (100-149)
            [6.3, 3.3, 6.0, 2.5, 2], [5.8, 2.7, 5.1, 1.9, 2], [7.1, 3.0, 5.9, 2.1, 2], [6.3, 2.9, 5.6, 1.8, 2], [6.5, 3.0, 5.8, 2.2, 2],
            [7.6, 3.0, 6.6, 2.1, 2], [4.9, 2.5, 4.5, 1.7, 2], [7.3, 2.9, 6.3, 1.8, 2], [6.7, 2.5, 5.8, 1.8, 2], [7.2, 3.6, 6.1, 2.5, 2],
            [6.5, 3.2, 5.1, 2.0, 2], [6.4, 2.7, 5.3, 1.9, 2], [6.8, 3.0, 5.5, 2.1, 2], [5.7, 2.5, 5.0, 2.0, 2], [5.8, 2.8, 5.1, 2.4, 2],
            [6.4, 3.2, 5.3, 2.3, 2], [6.5, 3.0, 5.5, 1.8, 2], [7.7, 3.8, 6.7, 2.2, 2], [7.7, 2.6, 6.9, 2.3, 2], [6.0, 2.2, 5.0, 1.5, 2],
            [6.9, 3.2, 5.7, 2.3, 2], [5.6, 2.8, 4.9, 2.0, 2], [7.7, 2.8, 6.7, 2.0, 2], [6.3, 2.7, 4.9, 1.8, 2], [6.7, 3.3, 5.7, 2.1, 2],
            [7.2, 3.2, 6.0, 1.8, 2], [6.2, 2.8, 4.8, 1.8, 2], [6.1, 3.0, 4.9, 1.8, 2], [6.4, 2.8, 5.6, 2.1, 2], [7.2, 3.0, 5.8, 1.6, 2],
            [7.4, 2.8, 6.1, 1.9, 2], [7.9, 3.8, 6.4, 2.0, 2], [6.4, 2.8, 5.6, 2.2, 2], [6.3, 2.8, 5.1, 1.5, 2], [6.1, 2.6, 5.6, 1.4, 2],
            [7.7, 3.0, 6.1, 2.3, 2], [6.3, 3.4, 5.6, 2.4, 2], [6.4, 3.1, 5.5, 1.8, 2], [6.0, 3.0, 5.5, 1.8, 2], [6.9, 3.1, 5.4, 2.1, 2],
            [6.7, 3.1, 5.6, 2.4, 2], [6.9, 3.1, 5.1, 2.3, 2], [5.8, 2.7, 5.1, 1.9, 2], [6.8, 3.2, 5.9, 2.3, 2], [6.7, 3.3, 5.7, 2.5, 2],
            [6.7, 3.0, 5.2, 2.3, 2], [6.3, 2.5, 5.0, 1.9, 2], [6.5, 3.0, 5.2, 2.0, 2], [6.2, 3.4, 5.4, 2.3, 2], [5.9, 3.0, 5.1, 1.8, 2]
        ];

        // Calculate Dataset Means
        const datasetMeans = [
            (rawIrisData.reduce((acc, cur) => acc + cur[0], 0) / 150).toFixed(2),
            (rawIrisData.reduce((acc, cur) => acc + cur[1], 0) / 150).toFixed(2),
            (rawIrisData.reduce((acc, cur) => acc + cur[2], 0) / 150).toFixed(2),
            (rawIrisData.reduce((acc, cur) => acc + cur[3], 0) / 150).toFixed(2)
        ];

        const speciesNames = ['Setosa', 'Versicolor', 'Virginica'];
        let comparisonChartInstance = null;

        // Initialize on load
        window.addEventListener('DOMContentLoaded', () => {
            initChart();
            onSliderChange();
        });

        // KNN Classifier algorithm implementation (k=5)
        function classifyKNN(sl, sw, pl, pw, k = 5) {
            const distances = rawIrisData.map(item => {
                const dist = Math.sqrt(
                    Math.pow(item[0] - sl, 2) +
                    Math.pow(item[1] - sw, 2) +
                    Math.pow(item[2] - pl, 2) +
                    Math.pow(item[3] - pw, 2)
                );
                return { dist, target: item[4] };
            });

            distances.sort((a, b) => a.dist - b.dist);
            const neighbors = distances.slice(0, k);

            const counts = { 0: 0, 1: 0, 2: 0 };
            neighbors.forEach(n => counts[n.target]++);

            const probs = {
                0: (counts[0] / k) * 100,
                1: (counts[1] / k) * 100,
                2: (counts[2] / k) * 100
            };

            let bestClass = 0;
            let maxVotes = -1;
            for (let c in counts) {
                if (counts[c] > maxVotes) {
                    maxVotes = counts[c];
                    bestClass = parseInt(c);
                }
            }

            return {
                predictedClass: bestClass,
                probabilities: probs,
                confidence: probs[bestClass]
            };
        }

        // Slider change handler
        function onSliderChange() {
            const sl = parseFloat(document.getElementById('input-sl').value);
            const sw = parseFloat(document.getElementById('input-sw').value);
            const pl = parseFloat(document.getElementById('input-pl').value);
            const pw = parseFloat(document.getElementById('input-pw').value);

            // Update badge text values
            document.getElementById('val-sl').innerText = sl.toFixed(1) + ' cm';
            document.getElementById('val-sw').innerText = sw.toFixed(1) + ' cm';
            document.getElementById('val-pl').innerText = pl.toFixed(1) + ' cm';
            document.getElementById('val-pw').innerText = pw.toFixed(1) + ' cm';

            // Run KNN prediction
            const result = classifyKNN(sl, sw, pl, pw, 5);

            // Update Prediction UI
            document.getElementById('pred-species').innerText = speciesNames[result.predictedClass];
            document.getElementById('pred-confidence').innerText = result.confidence.toFixed(1) + '%';

            // Update Probability Bars
            for (let i = 0; i < 3; i++) {
                const p = result.probabilities[i];
                document.getElementById(`prob-val-${i}`).innerText = p.toFixed(1) + '%';
                document.getElementById(`prob-bar-${i}`).style.width = p + '%';
            }

            // Update Comparison Chart Data
            if (comparisonChartInstance) {
                comparisonChartInstance.data.datasets[0].data = [sl, sw, pl, pw];
                comparisonChartInstance.update();
            }
        }

        // Initialize Comparison Bar Chart with Chart.js
        function initChart() {
            const ctx = document.getElementById('comparisonChart').getContext('2d');
            comparisonChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'],
                    datasets: [
                        {
                            label: 'Your Values',
                            data: [5.0, 3.5, 3.1, 0.6],
                            backgroundColor: '#ec4899',
                            borderRadius: 8,
                            barThickness: 28
                        },
                        {
                            label: 'Dataset Average',
                            data: datasetMeans,
                            backgroundColor: '#fbcfe8',
                            borderRadius: 8,
                            barThickness: 28
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y} cm`
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { display: false },
                            ticks: { color: '#64748b', font: { family: 'Inter', size: 11 } }
                        },
                        y: {
                            grid: { color: 'rgba(236, 72, 153, 0.05)' },
                            ticks: { color: '#64748b', font: { family: 'Inter', size: 11 } },
                            min: 0,
                            max: 8
                        }
                    }
                }
            });
        }

        // Randomize Sample button
        function randomizeSample() {
            const randType = Math.floor(Math.random() * 3);
            let sample;
            if (randType === 0) {
                sample = [5.1 + Math.random()*0.8, 3.3 + Math.random()*0.6, 1.4 + Math.random()*0.4, 0.2 + Math.random()*0.2];
            } else if (randType === 1) {
                sample = [5.9 + Math.random()*1.0, 2.7 + Math.random()*0.6, 4.2 + Math.random()*0.9, 1.3 + Math.random()*0.5];
            } else {
                sample = [6.5 + Math.random()*1.2, 3.0 + Math.random()*0.6, 5.5 + Math.random()*1.2, 2.0 + Math.random()*0.5];
            }

            document.getElementById('input-sl').value = sample[0].toFixed(1);
            document.getElementById('input-sw').value = sample[1].toFixed(1);
            document.getElementById('input-pl').value = sample[2].toFixed(1);
            document.getElementById('input-pw').value = sample[3].toFixed(1);

            onSliderChange();
        }

        // Reset Sliders
        function resetSliders() {
            document.getElementById('input-sl').value = 5.0;
            document.getElementById('input-sw').value = 3.5;
            document.getElementById('input-pl').value = 3.1;
            document.getElementById('input-pw').value = 0.6;
            onSliderChange();
        }

        // Deploy modal placeholder action
        function triggerDeployModal() {
            alert("🌸 Pink Streamlit Web App deployed successfully! Model endpoint is active.");
        }
    </script>
</body>
</html>