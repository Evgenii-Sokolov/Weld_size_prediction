# Weld_size_prediction
Приложение для прогнозирования размеров сварного шва при электронно-лучевой сварке тонкостенных конструкций аэрокосмического назначения.
Приложение прогнозирует размеры сварных швов: Глубину (Depth), Ширину (Width).

Для прогнозирования в приложение необходимо ввести:
1. Величину сварочного тока (IW)
2. Величину тока фокусировки электронного пучка (IF)
3. Скорость сварки (VW)
4. Расстояние от поверхности образцов до электронно-оптической системы (FP)


В основу приложения заложена модель машинного обучения RandomForestRegressor обученная на экспериментальных данны. Подробнее с моделью можно ознакомиться в Jupyter Notebook, вложенным в материалы приложения. 