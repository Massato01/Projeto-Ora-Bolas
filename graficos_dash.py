import dash
from dash      import dcc, html
from visual_3d import *



def plotar_grafico_dash():
    '''
    ============================================
             PLOTA UM GRÁFICO COM DASH
    ============================================
    titulo: título do gráfico
    x: valores do eixo X
    y: valores do eixo Y
    xlabel: titulo do eixo X
    ylabel: titulo do eixo Y

    return -> gráfico de acordo com parâmetros
              passados
    '''
    app = dash.Dash()
    app.layout = html.Div(
    [
        dcc.Dropdown(
            id = 'graph-type', # component_id
            options = [
                {'label' : 'Trajetória da Bola em X(t)',
                 'value' : 'traj_bolaX'},

                {'label' : 'Trajetória da Bola em Y(t)',
                 'value' : 'traj_bolaY'},

                {'label' : 'Velocidade da Bola',
                 'value' : 'velocidade_bola'},

                {'label' : 'Aceleracao da Bola',
                  'value' : 'aceleracao_bola'},

                {'label' : 'Trajetoria do Robô em X(t)',
                 'value' : 'traj_roboX'},

                {'label' : 'Trajetoria do Robô em Y(t)',
                 'value' : 'traj_roboY'},

                {'label' : 'Velocidade do Robô',
                 'value' : 'velocidade_robo'},

                {'label' : 'Aceleração do Robô',
                 'value' : 'aceleracao_robo'},

                {'label' : 'VX do Robô',
                 'value' : 'VX_robo'},

                {'label' : 'VY do Robô',
                 'value' : 'VY_robo'},

                {'label' : 'AX do Robô',
                 'value' : 'AX_robo'},

                {'label' : 'AY do Robô',
                 'value' : 'AY_robo'},

                {'label' : 'Robô e Bola em um plano',
                 'value' : 'robo_bola_plano'},

                {'label' : 'Distância entre o Robô e a Bola em T',
                 'value' : 'dist_robo_bola'}
            ],
            value = 'traj_bolaX' # Default value
        ),

        dcc.Graph(id = 'graph') # component_id

    ], style = {'backgroundColor' : '#FAFBFF',
                'fontFamily' : 'Cascadia Code',
                'border' : '2px #5B0FFF solid',
                'borderRadius' : '10px',
                'padding' : '10px',
                # 'marginRight' : '10%',
                # 'marginLeft' : '10%',
                # 'marginTop' : '10%',
                'margin' : '10%'}
    )

    # ----- Callback of the Dropdown choice to Graph -----
    @app.callback(Output(component_id='graph', component_property='figure'),
                [Input(component_id='graph-type', component_property='value')])
    # ----------------------------------------------------


    # ===== DYNAMIC FUNCTION FOR THE CHANGE OF PLOTS =====
    def update_figure(selected_type):
        #  ----------------- Trajetoria da Bola ----------------
        if selected_type == 'traj_bolaX':
            return {'data' : [
                    go.Scatter(
                        x = bola_t_pos,
                        y = bola_x_pos,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        # marker = {
                        #     'color' : '#5B0FFF', #5B0FFF
                        #     'size' : 12,
                        #     'symbol' : 'circle-open-dot',
                        #     'line' : {'width' : 2}
                        #     }
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Trajetória da Bola em X(t)<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t/s<i><b>'},
                                yaxis = {'title' : f'<b>x/m<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        # -----------------------------------------------

        # ----------------- LINE PLOT -------------------
        elif selected_type == 'traj_bolaY':
            return {'data' : [
                        go.Scatter(
                            x = bola_t_pos,
                            y = bola_y_pos,
                            mode = 'lines',
                            marker = {'color' : '#5B0FFF'}
                            )
                        ],

                        'layout' : go.Layout(
                                    title = '<b>Trajetória da Bola em Y(t)<b>',
                                    font = {'color' : 'black'},
                                    xaxis = {'title' : f'<b><i>t/s<i><b>'},
                                    yaxis = {'title' : f'<b>y/m<b>'},
                                    plot_bgcolor = '#FAFBFF',
                                    paper_bgcolor = '#FAFBFF'
                                    )              
                    }
        
        elif selected_type == 'velocidade_bola':
            return {'data' : [
                    go.Scatter(
                        x = [0, 0],
                        y = [0, 0],
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Velocidade da Bola<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t/s<i><b>'},
                                yaxis = {'title' : f'<b>x/m<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        
        elif selected_type == 'aceleracao_bola':
            return {'data' : [
                    go.Scatter(
                        x = [0, 0],
                        y = [0, 0],
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Aceleração da Bola<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t/s<i><b>'},
                                yaxis = {'title' : f'<b>x/m<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        
        # TRAJETORIA DO ROBO EM X
        elif selected_type == 'traj_roboX':
            return {'data' : [
                    go.Scatter(
                        x = intercepto_tRobo,
                        y = intercepto_xRobo,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Trajetória do Robô em X(t)<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t/s<i><b>'},
                                yaxis = {'title' : f'<b>x/m<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        
        # TRAJETORIA DO ROBO EM Y
        elif selected_type == 'traj_roboY':
            return {'data' : [
                    go.Scatter(
                        x = intercepto_tRobo,
                        y = intercepto_yRobo,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Trajetória do Robô em Y(t)<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t/s<i><b>'},
                                yaxis = {'title' : f'<b>y/m<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        
        # VELOCIDADE DO ROBO
        elif selected_type == 'velocidade_robo':
            return {'data' : [
                    go.Scatter(
                        x = lista_tempo,
                        y = velocidade_robo,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Velocidade do Robô em função do Tempo<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>s<i><b>'},
                                yaxis = {'title' : f'<b>m/s<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        
        # ACELERAÇÃO DO ROBO
        elif selected_type == 'aceleracao_robo':
            return {'data' : [
                    go.Scatter(
                        x = lista_tempo,
                        y = aceleracao_robo,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>Aceleração do Robô em função do Tempo<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>s<i><b>'},
                                yaxis = {'title' : f'<b>m/s²<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
            
        # # VX DO ROBO
        # elif selected_type == 'VX_robo':
        #     return {'data' : [
        #             go.Scatter(
        #                 x = lista_tempo,
        #                 y = vx_robo,
        #                 mode = 'lines',
        #                 marker = {'color' : '#5B0FFF'}
        #                 )
        #             ],

        #             'layout' : go.Layout(
        #                         title = '<b>VX do Robô<b>',
        #                         font = {'color' : 'black'},
        #                         xaxis = {'title' : f'<b><i>t(s)<i><b>'},
        #                         yaxis = {'title' : f'<b>Vx(m/s)<b>'},
        #                         plot_bgcolor = '#FAFBFF',
        #                         paper_bgcolor = '#FAFBFF'
        #                         )              
        #         }
        
        # # VY DO ROBO
        # if selected_type == 'VY_robo':
        #     return {'data' : [
        #                 go.Scatter(
        #                     x = lista_tempo,
        #                     y = vy_robo,
        #                     mode = 'lines',
        #                     marker = {'color' : '#5B0FFF'}
        #                     )
        #                 ],

        #                 'layout' : go.Layout(
        #                             title = '<b>VY do Robô<b>',
        #                             font = {'color' : 'black'},
        #                             xaxis = {'title' : f'<b><i>t(s)<i><b>'},
        #                             yaxis = {'title' : f'<b>Vy(m/s)<b>'},
        #                             plot_bgcolor = '#FAFBFF',
        #                             paper_bgcolor = '#FAFBFF'
        #                             )              
        #             }

        # AX DO ROBO
        elif selected_type == 'AX_robo':
            return {'data' : [
                    go.Scatter(
                        x = lista_tempo,
                        y = ax_robo,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>AX do Robô<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t(s)<i><b>'},
                                yaxis = {'title' : f'<b>Ax(m/s²)<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }
        
        elif selected_type == 'AY_robo':
            return {'data' : [
                    go.Scatter(
                        x = lista_tempo,
                        y = ay_robo,
                        mode = 'lines',
                        marker = {'color' : '#5B0FFF'}
                        )
                    ],

                    'layout' : go.Layout(
                                title = '<b>AY do Robô<b>',
                                font = {'color' : 'black'},
                                xaxis = {'title' : f'<b><i>t(s)<i><b>'},
                                yaxis = {'title' : f'<b>AY(m/s²)<b>'},
                                plot_bgcolor = '#FAFBFF',
                                paper_bgcolor = '#FAFBFF'
                                )              
                }


    # -----------------------------------------------

    return app.run_server()


# plotar_grafico_dash()
